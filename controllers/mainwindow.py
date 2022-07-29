from PyQt5.QtWidgets import QFileDialog
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from views.VentanaPrincipal import Ventana_Principal

PATH = None

class MainWindow(QWidget, Ventana_Principal):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.boton_integrantes.clicked.connect(self.integrantes)
        self.boton_gauss.clicked.connect(self.obtenerMatriz)

    def obtenerMatriz(self):   
        from controllers.VentanaGauss import GaussWindow
        window = GaussWindow(self)
        self.close()
        window.show()

    def integrantes(self):
        from controllers.VentanaIntegrantes import IntegrantesWindow
        window = IntegrantesWindow(self)
        self.close()
        window.show()