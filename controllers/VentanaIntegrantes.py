from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from views.VentanaIntegrantes import VentanaIntegrantes

class IntegrantesWindow(QWidget, VentanaIntegrantes):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowFlag(Qt.Window)
        self.boton_home.clicked.connect(self.home)

    
    def interfaz(self):
        pass

    def algoritmo(self):
        pass

    def lectura(self):
        pass
    
    def home(self):
        from controllers.mainwindow import MainWindow
        window = MainWindow(self)
        self.close()
        window.show()

    