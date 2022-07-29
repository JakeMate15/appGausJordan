# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Form_error2(object):
    def setupUi(self, Form_error2):
        if not Form_error2.objectName():
            Form_error2.setObjectName(u"Form_error2")
        Form_error2.resize(467, 404)
        Form_error2.setStyleSheet(u"background-color: rgb(29, 34, 38);")
        self.label_error1 = QLabel(Form_error2)
        self.label_error1.setObjectName(u"label_error1")
        self.label_error1.setGeometry(QRect(20, 40, 431, 111))
        self.textBrowser_error2 = QTextBrowser(Form_error2)
        self.textBrowser_error2.setObjectName(u"textBrowser_error2")
        self.textBrowser_error2.setGeometry(QRect(120, 210, 241, 91))

        self.retranslateUi(Form_error2)

        QMetaObject.connectSlotsByName(Form_error2)
    # setupUi

    def retranslateUi(self, Form_error2):
        Form_error2.setWindowTitle(QCoreApplication.translate("Form_error2", u"Form", None))
        self.label_error1.setText(QCoreApplication.translate("Form_error2", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">HA INTRODUCIDO UNO O M\u00c1S CARACTERES INCOMPATIBLES</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">LAS COORDENADAS SON:</span></p></body></html>", None))
    # retranslateUi

