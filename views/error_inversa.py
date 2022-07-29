# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_inversa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Form_error_inversa(object):
    def setupUi(self, Form_error_inversa):
        if not Form_error_inversa.objectName():
            Form_error_inversa.setObjectName(u"Form_error_inversa")
        Form_error_inversa.resize(467, 404)
        Form_error_inversa.setStyleSheet(u"background-color: rgb(29, 34, 38);")
        self.label_error_inversa = QLabel(Form_error_inversa)
        self.label_error_inversa.setObjectName(u"label_error_inversa")
        self.label_error_inversa.setGeometry(QRect(10, 130, 431, 111))

        self.retranslateUi(Form_error_inversa)

        QMetaObject.connectSlotsByName(Form_error_inversa)
    # setupUi

    def retranslateUi(self, Form_error_inversa):
        Form_error_inversa.setWindowTitle(QCoreApplication.translate("Form_error_inversa", u"Form", None))
        self.label_error_inversa.setText(QCoreApplication.translate("Form_error_inversa", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">LA MATRIZ NO TIENE INVERSA</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">CIERRE ESTE CUADRO PARA CONTINUAR</span></p></body></html>", None))
    # retranslateUi

