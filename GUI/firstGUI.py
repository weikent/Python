# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstGUI.ui'
#
# Created: Wed Sep  3 11:16:04 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 60, 93, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 190, 751, 341))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.SSID_Label = QtGui.QLabel(self.gridLayoutWidget)
        self.SSID_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.SSID_Label.setObjectName(_fromUtf8("SSID_Label"))
        self.gridLayout.addWidget(self.SSID_Label, 0, 0, 1, 1)
        self.Pwd_Label = QtGui.QLabel(self.gridLayoutWidget)
        self.Pwd_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Pwd_Label.setObjectName(_fromUtf8("Pwd_Label"))
        self.gridLayout.addWidget(self.Pwd_Label, 1, 0, 1, 1)
        self.SSID_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.SSID_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SSID_lineEdit.setObjectName(_fromUtf8("SSID_lineEdit"))
        self.gridLayout.addWidget(self.SSID_lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Pair", None, QtGui.QApplication.UnicodeUTF8))
        self.SSID_Label.setText(QtGui.QApplication.translate("MainWindow", "SSID:", None, QtGui.QApplication.UnicodeUTF8))
        self.Pwd_Label.setText(QtGui.QApplication.translate("MainWindow", "PassWord:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

