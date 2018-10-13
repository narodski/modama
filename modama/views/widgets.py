from flask_appbuilder.widgets import ShowWidget, ListWidget
import logging


log = logging.getLogger(__name__)


class ModamaShowWidget(ShowWidget):
    template = 'general/widgets/show.html'

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __call__(self, related=False, **kwargs):
        if(related is True and 'pk' in kwargs.keys() and
           'pk' in self.template_args.keys()):
            del kwargs['pk']
        return super().__call__(**kwargs)


class ShowPrintWidget(ShowWidget):
    template = 'general/widgets/showprint.html'


class ListPrintWidget(ListWidget):
    template = 'general/widgets/listprint.html'
