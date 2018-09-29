from flask_appbuilder.widgets import ShowWidget, ListWidget


class ShowPrintWidget(ShowWidget):
    template = 'general/widgets/showprint.html'


class ListPrintWidget(ListWidget):
    template = 'general/widgets/listprint.html'
