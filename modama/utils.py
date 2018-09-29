from flask import Markup
import os.path as op
import flask_appbuilder as fab


def get_global_static_path(appbuilder):
    return op.join(
        get_fab_path(),
        appbuilder.static_folder)


def get_fab_path():
    return op.abspath(op.dirname(fab.__file__))


def get_img_upload_url(appbuilder):
    return appbuilder.app.config['IMG_UPLOAD_URL']


def get_img_upload_path(appbuilder):
    return op.join(
        get_fab_path(),
        appbuilder.app.config['IMG_UPLOAD_FOLDER'])


def make_image(img_url, link_url, alt='Photo'):
    if img_url is not None:
        return Markup('<a href="' + link_url + '" class="thumbnail">' +
                      '<img src="' + img_url + '" alt="' + alt +
                      '" class="img-rounded img-responsive"></a>')
    else:
        return Markup('<a href="' + link_url + '" class="thumbnail">' +
                      '<img src="//:0" alt="' + alt +
                      '" class="img-responsive"></a>')
