from wtforms.widgets import HTMLString, html_params
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget


class StaticTextWidget:
    def __init__(self, html, **kwargs):
        self.html = html
        self.readonly = True

    def __call__(self, field, **kwargs):
        return self.html

class ROTextFieldWidget(BS3TextFieldWidget):
    """
    Read only textField Widget.
    """
    def __call__(self, field, **kwargs):
        kwargs['readonly'] = 'true'
        return super(ROTextFieldWidget, self).__call__(field, **kwargs)


class DateTimeTZPickerWidget(object):
    """
    Date Time picker from Eonasdan GitHub

    """
    data_template = ("""
<div class="input-group date modama_datetime" id="datetimepicker">
    <span class="input-group-addon">
        <i class="fa fa-calendar cursor-hand"></i>
    </span>
    <input class="form-control" data-format="YYYY-MM-DD HH:mm:ssZZ" %(text)s/>
</div>""")

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        if not field.data:
            field.data = ""
        template = self.data_template

        return HTMLString(template % {'text': html_params(type='text',
                                                          value=field.data,
                                                          **kwargs)})
