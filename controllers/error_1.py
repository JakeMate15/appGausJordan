from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from views.error1 import Form_error1


class error1(QWidget, Form_error1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
    
