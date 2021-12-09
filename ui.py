# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\axis9\Desktop\зыков\calen.ui'
#
# Created: Sun Nov 28 16:09:59 2021
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
from PySide2.QtWidgets import  *

from PySide2 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1115, 319)
        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 110, 352, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QCalendarWidget(Form)
        self.calendarWidget_2.setGeometry(QtCore.QRect(750, 100, 352, 201))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.checkBox.setObjectName("checkBox")
        self.label = QLabel(Form)
        self.label.setGeometry(QtCore.QRect(650, 90, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(520, 90, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Зыков", "Зыков", None))
        self.checkBox.setText(QApplication.translate("Form", "Включая текущую дату", None))
        self.label.setText(QApplication.translate("Form", "день/дней", None))
        self.label_2.setText(QApplication.translate("Form", "лет", None))
        self.label_3.setText(QApplication.translate("Form", "месяцев", None))
        self.label_4.setText(QApplication.translate("Form", "недель", None))
        self.label_5.setText(QApplication.translate("Form", "день/дней", None))



