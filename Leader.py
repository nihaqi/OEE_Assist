# -*- coding: utf-8 -*-

"""
Module implementing LeaderAct.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_Leader import Ui_MainWindow


class LeaderAct(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=Ui_MainWindow):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LeaderAct, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_actionExit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
