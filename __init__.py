from Ui import Ui_LoginWin, Ui_LeaderWin
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWin = QtWidgets.QMainWindow()
    #LeaderWin=QtWidgets.QMainWindow()
    
    ui_login = Ui_LoginWin()
    ui_login.setupUi(LoginWin)
    
    
    #LeaderWin.show()
    LoginWin.show()
    sys.exit(app.exec_())
