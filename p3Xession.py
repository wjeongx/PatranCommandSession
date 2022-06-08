from fileinput import filename
import sys
from PyQt5.QtWidgets import QApplication, QToolTip, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PatranCommandSession import modeling
from PatranCommandSession import Fields
from PatranCommandSession import p3Utilities
from PatranCommandSession import Loads
from PatranCommandSession import LoadCases
from PatranCommandSession import Result

#from Loads import Load

class Xession(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Patran Session Generator')
        self.setWindowIcon(QIcon('patran.png'))
        self.move(300, 300)
        self.resize(400, 400)

        btnModeling = QPushButton('Modeling', self)
        btnFEMField = QPushButton('FEM Field', self)
        btnLoad = QPushButton('Loads', self)
        btnLoadCase = QPushButton('Load Cases', self)
        btnResultCombine = QPushButton('Rsult Combine', self)
        btnResultSum = QPushButton('Result Sum', self)
        btnQuit = QPushButton('Quit', self)

        # btnLoad.setToolTip('This is a <b>QWidget</b> widget1')
        # btnLoad = QPushButton('Button2', self)
        # btn2.setToolTip('This is a <b>QWidget</b> widget2')
        # btn.setToolTip('This is a <b>QWidget</b> widget')

        btnModeling.move(50, 50)
        btnFEMField.move(50, 100)
        btnLoad.move(50, 150)
        btnLoadCase.move(50,200)
        btnResultCombine.move(50, 250)
        btnResultSum.move(50,300)
        btnQuit.move(50, 350)

        btnModeling.resize(300, 30)
        btnFEMField.resize(300, 30)
        btnLoad.resize(300, 30)
        btnLoadCase.resize(300,30)
        btnResultCombine.resize(300, 30)
        btnResultSum.resize(300, 30)

        btnQuit.resize(300, 30)

        btnModeling.clicked.connect(self.btnModelingClick)
        btnFEMField.clicked.connect(self.btnFEMFieldClick)
        btnLoad.clicked.connect(self.btnLoadClick)
        btnLoadCase.clicked.connect(self.btnLoadCaseClick)        
        btnResultCombine.clicked.connect(self.btnResultCombineClick)
        btnResultSum.clicked.connect(self.btnResultSumClick)
        btnQuit.clicked.connect(QApplication.instance().quit)

        #btn.resize(btn.sizeHint())

        self.show()

    def btnModelingClick(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './*fem input.xlsx')
        if filename[0] !='':
            modeling.joint_modeling(filename[0])
        else:
            return -1

    def btnFEMFieldClick(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './*field input.xlsx')
        print(filename[0])
        if filename[0] != '':
            Fields.FEMField(filename[0])
        else:
            return -1


    def btnLoadClick(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './*load input.xlsx')
        print('==============')
        print(filename[0])
        print('==============')
        if filename[0] != '':
            Loads.load_gen(filename[0])
        else:
            return -1
    
    def btnLoadCaseClick(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './*loadcases input.xlsx')
        
        if filename[0] != '':
            LoadCases.LoadCase(filename[0])
        else:
            return -1

    def btnResultCombineClick(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './*result input.xlsx')
        if filename[0] != '':
            Result.result_combine(filename[0])
        else:
            return -1

    def btnResultSumClick(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './*result input.xlsx')
        if filename[0] != '':
            Result.result_sum(filename[0])
        else:
            return -1

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Xession()
   sys.exit(app.exec_())


