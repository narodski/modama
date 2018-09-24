from flask_appbuilder import SimpleFormView
from flask import request
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from flask_appbuilder.forms import DynamicForm
import json
from .. import appbuilder
from flask_babel import lazy_gettext as _
from flask import flash, redirect, url_for
from ..formService import FormService
from zipfile import ZipFile
import logging
from modama.models.common import MyUser
from modama.exceptions import (UnkownFormError, ValidationError,
                               UnkownDatasetError)
from modama import db
from sqlalchemy.exc import IntegrityError

log = logging.getLogger(__name__)


class UploadForm(DynamicForm):
    file = FileField(validators=[FileRequired(), FileAllowed(('zip',))])


class UploadView(SimpleFormView):

    form = UploadForm
    form_title = 'Upload'
    message = 'Data uploaded successfully'

    def form_post(self, form):
        f = form.file.data
        filename = secure_filename(f.filename)
        log.debug('Got zipfile {}'.format(filename))
        zf = ZipFile(f)
        upload_success = 0
        for rf in zf.namelist():
            if rf.endswith('.json'):
                report_name = rf.replace('.json', '')
                log.info('Processing report {} upload.'.format(report_name))
                log.debug("Opening file {}".format(rf))
                try:
                    jf = json.loads(zf.open(rf, 'r').read()
                                    .decode(request.charset))
                except json.decoder.JSONDecodeError as e:
                    log.error(e)
                    flash('File {} does not contain a valid report'.format(rf),
                          'danger')
                    continue
                log.debug('Got data {}'.format(jf))
                req = set(['form', 'dataset', 'report_id', 'formdata',
                           'user_id', 'device_id'])
                if not req <= set(jf.keys()):
                    log.error('Not all required keys are available in {}.'
                              .format(rf))
                    flash('File {} does not contain a valid report'.format(rf),
                          'danger')
                    continue
                formname = jf['form']
                datasetname = jf['dataset']
                formdata = jf['formdata']
                formdata['report_id'] = jf['report_id']
                formdata['device_id'] = jf['device_id']
                userid = int(jf['user_id'])
                args = {'formname': formname, 'rf': rf,
                        'reportid': jf['report_id'],
                        'userid': userid}
                user = db.session.query(MyUser).get(userid)
                if user is None:
                    flash("User {userid} not found in report {reportid}"
                          .format(**args), 'danger')
                    continue
                try:
                    view = FormService.getView(datasetname, formname)
                except (UnkownDatasetError, UnkownFormError) as e:
                    log.error("Failed uploading file {rf} due to error"
                              .format(**args))
                    log.error(e)
                    flash("Failed to upload file {rf}. ".format(**args) +
                          "The form {formname} does not ".format(**args) +
                          "exist or you don't have access to it.", 'danger')
                    continue
                try:
                    instance = FormService.processView(view, formdata)
                except ValidationError as e:
                    log.error(e)
                    flash("Failed uploading file {rf} due to a ".format(**args)
                          + "validation error: {}".format(e),
                          'danger')
                    continue
                instance.created_by = user
                try:
                    FormService.saveInstance(instance)
                except IntegrityError as e:
                    if "duplicate key" in str(e) and "report_id" in str(e):
                        flash("Report {reportid} ".format(**args) +
                              "has already been uploaded.", 'warning')
                    else:
                        log.error(e)
                        flash("Something went wrong when uploading report " +
                              "{reportid}".format(**args), 'danger')
                    continue
                flash('Uploaded {reportid} successfully.'.format(**args),
                      'success')
                upload_success += 1

            else:
                log.warning('{} is not a json file'.format(rf))
        if upload_success == 0:
            flash("No valid reports found in file.", "warning")
        else:
            flash("Uploaded {} reports successfully".format(upload_success),
                  'info')
        self.update_redirect()
        return redirect(url_for('UploadView.this_form_get'))


appbuilder.add_view(UploadView, "Upload Data", label=_("Upload data"),
                    category='Upload')
