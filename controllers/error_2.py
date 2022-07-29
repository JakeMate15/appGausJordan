from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from views.error2 import Form_error2


class error2(QWidget, Form_error2):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)    
