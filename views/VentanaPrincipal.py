# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ventana_Principal(object):
    def setupUi(self, Ventana_Principal):
        if not Ventana_Principal.objectName():
            Ventana_Principal.setObjectName(u"Ventana_Principal")
        Ventana_Principal.resize(1074, 533)
        Ventana_Principal.setStyleSheet(u"background-color: rgb(29, 34, 38);")
        self.frame = QFrame(Ventana_Principal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 340, 1071, 191))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.boton_gauss = QPushButton(self.frame)
        self.boton_gauss.setObjectName(u"boton_gauss")
        self.boton_gauss.setGeometry(QRect(500, 30, 81, 81))
        self.boton_gauss.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_gauss.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#5c5c5c;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/obtenermatriz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_gauss.setIcon(icon)
        self.boton_gauss.setIconSize(QSize(81, 81))
        self.boton_gauss.setFlat(True)
        self.label_obtener_matriz = QLabel(self.frame)
        self.label_obtener_matriz.setObjectName(u"label_obtener_matriz")
        self.label_obtener_matriz.setGeometry(QRect(490, 110, 111, 16))
        self.label_integrantes = QLabel(self.frame)
        self.label_integrantes.setObjectName(u"label_integrantes")
        self.label_integrantes.setGeometry(QRect(950, 130, 121, 31))
        self.boton_integrantes = QPushButton(self.frame)
        self.boton_integrantes.setObjectName(u"boton_integrantes")
        self.boton_integrantes.setGeometry(QRect(980, 70, 61, 61))
        self.boton_integrantes.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_integrantes.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#5c5c5c;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/equipo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_integrantes.setIcon(icon1)
        self.boton_integrantes.setIconSize(QSize(61, 61))
        self.boton_integrantes.setFlat(True)
        self.label = QLabel(Ventana_Principal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 30, 451, 81))
        self.pushButton = QPushButton(Ventana_Principal)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 130, 271, 181))
        icon2 = QIcon()
        icon2.addFile(u"./assets/texto.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(241, 240))
        self.pushButton.setFlat(True)

        self.retranslateUi(Ventana_Principal)

        QMetaObject.connectSlotsByName(Ventana_Principal)
    # setupUi

    def retranslateUi(self, Ventana_Principal):
        Ventana_Principal.setWindowTitle(QCoreApplication.translate("Ventana_Principal", u"App Gauss-Jordan", None))
        self.boton_gauss.setText("")
        self.label_obtener_matriz.setText(QCoreApplication.translate("Ventana_Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">OBTENER MATRIZ</span></p></body></html>", None))
        self.label_integrantes.setText(QCoreApplication.translate("Ventana_Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#ffffff;\">INTEGRANTES</span></p></body></html>", None))
        self.boton_integrantes.setText("")
        self.label.setText(QCoreApplication.translate("Ventana_Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Antes de darle al bot\u00f3n &quot;Obtener Matriz&quot; </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">crea un archivo de texto con el nombre &quot;matriz.txt como el siguiente:</span></p></body></html>", None))
        self.pushButton.setText("")
    # retranslateUi

