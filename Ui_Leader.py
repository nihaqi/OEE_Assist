# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/allen/Documents/py_ws/login/Leader.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import Ui_login

class Ui_LeaderWin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        
       # self.parentwindow=QtWidgets.QMainWindow()
        #self.ui_login = Ui_login.Ui_MainWindow()
        #self.ui_login.setupUi(self.parentwindow)
        #self.actionLogout.triggered.connect(MainWindow.close)
       #self.actionLogout.triggered.connect(self.parentwindow.show)
        
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(MainWindow.close)

        self.actionCoefficient = QtWidgets.QAction(MainWindow)
        self.actionCoefficient.setObjectName("actionCoefficient")
        self.actionOpen_sql = QtWidgets.QAction(MainWindow)
        self.actionOpen_sql.setObjectName("actionOpen_sql")
        self.actionModel1 = QtWidgets.QAction(MainWindow)
        self.actionModel1.setObjectName("actionModel1")
        self.actionModel2 = QtWidgets.QAction(MainWindow)
        self.actionModel2.setObjectName("actionModel2")
        self.actionModel3 = QtWidgets.QAction(MainWindow)
        self.actionModel3.setObjectName("actionModel3")
        self.menuNew.addAction(self.actionModel1)
        self.menuNew.addAction(self.actionModel2)
        self.menuNew.addAction(self.actionModel3)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_sql)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionCoefficient)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCoefficient.setText(_translate("MainWindow", "Coefficient"))
        self.actionOpen_sql.setText(_translate("MainWindow", "Open(sql)"))
        self.actionModel1.setText(_translate("MainWindow", "Model1"))
        self.actionModel2.setText(_translate("MainWindow", "Model2"))
        self.actionModel3.setText(_translate("MainWindow", "Model3"))

