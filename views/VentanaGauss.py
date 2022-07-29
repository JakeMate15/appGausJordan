# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaGauss.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class VentanaGauss(object):
    def setupUi(self, VentanaGauss):
        if not VentanaGauss.objectName():
            VentanaGauss.setObjectName(u"VentanaGauss")
        VentanaGauss.resize(1074, 542)
        VentanaGauss.setStyleSheet(u"background-color: rgb(29, 34, 38);")
        self.label_ingresada = QLabel(VentanaGauss)
        self.label_ingresada.setObjectName(u"label_ingresada")
        self.label_ingresada.setGeometry(QRect(90, 80, 181, 31))
        self.label_resultado = QLabel(VentanaGauss)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setGeometry(QRect(800, 80, 181, 31))
        self.frame = QFrame(VentanaGauss)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 380, 1071, 151))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.boton_MGauss = QPushButton(self.frame)
        self.boton_MGauss.setObjectName(u"boton_MGauss")
        self.boton_MGauss.setGeometry(QRect(270, 10, 81, 81))
        self.boton_MGauss.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_MGauss.setStyleSheet(u"QPushButton:hover\n"
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
        icon = QIcon()
        icon.addFile(u"./assets/gauss.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_MGauss.setIcon(icon)
        self.boton_MGauss.setIconSize(QSize(81, 81))
        self.boton_MGauss.setFlat(True)
        self.label_MGauss = QLabel(self.frame)
        self.label_MGauss.setObjectName(u"label_MGauss")
        self.label_MGauss.setGeometry(QRect(200, 100, 221, 21))
        self.boton_home = QPushButton(self.frame)
        self.boton_home.setObjectName(u"boton_home")
        self.boton_home.setGeometry(QRect(10, 80, 71, 71))
        self.boton_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_home.setStyleSheet(u"QPushButton:hover\n"
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
        icon1.addFile(u"./assets/casa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_home.setIcon(icon1)
        self.boton_home.setIconSize(QSize(61, 61))
        self.boton_home.setFlat(True)
        self.label_inversa = QLabel(self.frame)
        self.label_inversa.setObjectName(u"label_inversa")
        self.label_inversa.setGeometry(QRect(440, 100, 221, 21))
        self.boton_inversa = QPushButton(self.frame)
        self.boton_inversa.setObjectName(u"boton_inversa")
        self.boton_inversa.setGeometry(QRect(490, 10, 121, 81))
        self.boton_inversa.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_inversa.setStyleSheet(u"QPushButton:hover\n"
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
        icon2 = QIcon()
        icon2.addFile(u"./assets/inversa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_inversa.setIcon(icon2)
        self.boton_inversa.setIconSize(QSize(95, 95))
        self.boton_inversa.setFlat(True)
        self.label_determinante = QLabel(self.frame)
        self.label_determinante.setObjectName(u"label_determinante")
        self.label_determinante.setGeometry(QRect(680, 100, 221, 21))
        self.boton_determinante = QPushButton(self.frame)
        self.boton_determinante.setObjectName(u"boton_determinante")
        self.boton_determinante.setGeometry(QRect(750, 10, 81, 81))
        self.boton_determinante.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_determinante.setStyleSheet(u"QPushButton:hover\n"
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
        icon3 = QIcon()
        icon3.addFile(u"./assets/determinante.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_determinante.setIcon(icon3)
        self.boton_determinante.setIconSize(QSize(81, 81))
        self.boton_determinante.setFlat(True)
        self.TEXT_matriz = QTextBrowser(VentanaGauss)
        self.TEXT_matriz.setObjectName(u"TEXT_matriz")
        self.TEXT_matriz.setGeometry(QRect(30, 130, 331, 231))
        self.TEXT_matriz.setAutoFillBackground(False)
        self.TEXT_matriz.setStyleSheet(u"")
        self.TEXT_matriz.setFrameShadow(QFrame.Plain)
        self.TEXT_matriz.setLineWidth(0)
        self.TEXT_resultado = QTextBrowser(VentanaGauss)
        self.TEXT_resultado.setObjectName(u"TEXT_resultado")
        self.TEXT_resultado.setGeometry(QRect(720, 130, 331, 231))
        self.TEXT_resultado.setLineWidth(0)

        self.retranslateUi(VentanaGauss)

        QMetaObject.connectSlotsByName(VentanaGauss)
    # setupUi

    def retranslateUi(self, VentanaGauss):
        VentanaGauss.setWindowTitle(QCoreApplication.translate("VentanaGauss", u"Form", None))
        self.label_ingresada.setText(QCoreApplication.translate("VentanaGauss", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">MATRIZ INGRESADA</span></p></body></html>", None))
        self.label_resultado.setText(QCoreApplication.translate("VentanaGauss", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">MATRIZ RESULTANTE</span></p></body></html>", None))
        self.boton_MGauss.setText("")
        self.label_MGauss.setText(QCoreApplication.translate("VentanaGauss", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">METODO GAUSS-JORDAN</span></p></body></html>", None))
        self.boton_home.setText("")
        self.label_inversa.setText(QCoreApplication.translate("VentanaGauss", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">MATRIZ INVERZA</span></p></body></html>", None))
        self.boton_inversa.setText("")
        self.label_determinante.setText(QCoreApplication.translate("VentanaGauss", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">DETERMINANTE</span></p></body></html>", None))
        self.boton_determinante.setText("")
        self.TEXT_matriz.setHtml(QCoreApplication.translate("VentanaGauss", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.TEXT_resultado.setHtml(QCoreApplication.translate("VentanaGauss", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

