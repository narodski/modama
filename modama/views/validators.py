from wtforms.validators import ValidationError
import logging

log = logging.getLogger(__name__)

class ValueRequired:
    def __init__(self, value, message=None):
        self.value = value
        self.message = message

    def __call__(self, form, field):
        log.debug("Value Required {}, field.data {}".format(field.data,
                                                            self.value))
        if field.data != self.value:
            raise ValidationError(self.message)
