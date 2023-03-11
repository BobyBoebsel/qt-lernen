from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog ,QWidget, QVBoxLayout, QTableWidget,QTableWidgetItem
from PyQt5.uic import loadUi
import sys
import openpyxl

a=2

class MainUI(QMainWindow):
    current_fontsize=8
    
    def __init__(self):
        super(MainUI,self).__init__()
        
        loadUi("Excel-Tool/excel.ui", self)
        self.current_Path= None
        #self.current_fontsize=8
        self.setWindowTitle("untitled")
        self.actionNew.triggered.connect(self.newfile)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.saveAs)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionOpen.triggered.connect(self.open)
        
        

    def newfile(self):
        #self.textEdit.clear()
        self.setWindowTitle("untitled")
        current_Path=None
    
    def save(self):
        if  self.current_Path is None:
            self.saveAs()
        else:
            with open(self.current_Path,'w') as fp:
                fp.write(self.textEdit.toPlainText())
                #fp.close()

    def open(self):
        fname = QFileDialog.getOpenFileName(self, "open File",'/', 'Text Files (*.txt)')
        self.setWindowTitle(fname[0])
        with open(fname[0],'r') as fp:
            filetext =fp.read()
            self.textEdit.setText(filetext)
            
        self.current_Path=fname[0]

        

    def saveAs(self):
        pathname=QFileDialog.getSaveFileName(self,'Open File','/','Text Files (*.txt)')
        with open(pathname[0],'w') as fp:
            fp.write(self.textEdit.toPlainText())
        self.current_Path=pathname[0]
        self.setWindowTitle(pathname[0])

    def undo(self):
        self.textEdit.undo()
    
    def redo(self):
        self.textEdit.redo()
    
    def copy(self):
        self.textEdit.copy()

    def paste(self):
        self.textEdit.paste()
    
    def cut(self):
        self.textEdit.cut()


   
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if a == 1:
        ui =MainUI()
        ui.show()
    else:
        mainwindow = MainUI()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(mainwindow)
        widget.setFixedHeight(850)
        widget.setFixedWidth(1120)
        widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print ("Exiting")

