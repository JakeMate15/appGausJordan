from views.error_filas import Form_error1
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt


class errorFilas(QWidget, Form_error1):
    def __init__ (self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
