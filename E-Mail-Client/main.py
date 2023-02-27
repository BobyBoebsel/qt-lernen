from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys
from email_sender import send_email

class MainUI(QMainWindow):
   
    
    def __init__(self):
        super(MainUI,self).__init__()
        
        loadUi("E-Mail-Client/main.ui", self)
        self.pushButton.clicked.connect(self.sendmail)
    
    def sendmail(self):
        send_email(recipient=self.lineEdit.text(),email=self.textEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui =MainUI()
    ui.show()
    app.exec_()