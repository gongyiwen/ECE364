#!/usr/bin/python
__author__ = 'ee364e03'

import sys

from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setAlignment(Qt.AlignRight)
        #self.textEdit.setCurrentCharFront(
        self.numberbuttons = [self.pushButton_0, self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4,
                        self.pushButton_5,self.pushButton_6,self.pushButton_7,self.pushButton_8,self.pushButton_9]
        for buttons in self.numberbuttons:
            buttons.clicked.connect(self.numberdisplay)
        self.pushButton_add.clicked.connect(self.addTo)
        self.pushButton_min.clicked.connect(self.subtractFrom)
        self.pushButton_mul.clicked.connect(self.mulTo)
        self.pushButton_div.clicked.connect(self.divFrom)
        self.pushButton_clear.clicked.connect(self.cleartext)
        self.pushButton_dot.clicked.connect(self.adddot)
        self.pushButton_equal.clicked.connect(self.produceresult)
        self.oprandtext=""
        self.oprandnum1=0

        self.oprandnum2=0
        self.oprator=""
        self.result=0
        self.equalflag=0
        self.decimal=self.comboBox.currentIndex()


    def numberdisplay(self):
        button = self.sender()
        self.decimal=int(self.comboBox.currentIndex())
        self.oprandtext=self.oprandtext+button.text()
        self.lineEdit.setText(self.oprandtext)
        self.equalflag=0

    def addTo(self):                     # 3 cases, 1+2+3, 1+2=3 3+1=4, 1++2=3
        print(self.oprator)
        print(self.equalflag)
        if self.oprator == "" and self.equalflag == 0: #it is the first operator,oprandnum2 is 0
            if not '.' in self.oprandtext:
                self.oprandnum1=int(self.lineEdit.displayText())
            else:
                self.oprandnum1=float(self.lineEdit.displayText())
            self.oprandtext=""
            self.oprator='+'
        elif self.oprator != "" and self.oprandtext !="":#didn't click = after one binary operation
            self.produceresult()
            self.oprator='+'
            self.equalflag=0
        else:#double click 2 operator
            self.oprandtext=""
            self.oprator='+'
        self.equalflag=0


    def subtractFrom(self):

        if self.oprator == "" and self.equalflag == 0:
            if not '.' in self.oprandtext:
                self.oprandnum1=int(self.oprandtext)
            else:
                self.oprandnum1=float(self.oprandtext)
            self.oprandtext=""
            self.oprator='-'
        elif self.oprator != "" and self.oprandtext !="":
            self.produceresult()
            self.oprator='-'
            self.equalflag=0
        else:
            self.oprandtext=""
            self.oprator='-'
        self.equalflag=0


    def mulTo(self):
        if self.oprator == "" and self.equalflag == 0:
            if not '.' in self.oprandtext:
                self.oprandnum1=int(self.oprandtext)
            else:
                self.oprandnum1=float(self.oprandtext)
            self.oprandtext=""
            self.oprator='*'
        elif self.oprator != "" and self.oprandtext !="":
            self.produceresult()
            self.oprator='*'
            self.equalflag=0
        else:

            self.oprandtext=""
            self.oprator='*'
        self.equalflag=0

    def divFrom(self):
        if self.oprator == "" and self.equalflag == 0:
            if not '.' in self.oprandtext:
                self.oprandnum1=int(self.oprandtext)
            else:
                self.oprandnum1=float(self.oprandtext)
            self.oprandtext=""
            self.oprator='/'
        elif self.oprator != "" and self.oprandtext !="":
            self.produceresult()
            self.oprator='/'
            self.equalflag=0
        else:
            self.oprandtext=""
            self.oprator='/'
        self.equalflag=0

    def cleartext(self):
        self.oprandnum2=0
        self.oprandnum1=0
        self.oprandtext=""
        self.oprator=""
        self.equalflag=0
        self.result=0
        self.lineEdit.setText('0')

    def adddot(self):
        if not '.' in self.oprandtext:
            self.oprandtext+='.'
            self.lineEdit.setText(self.oprandtext)

    def produceresult(self):#when hit =  case:1+3=4=4
        if self.equalflag == 0:
            if not '.' in self.oprandtext:
                self.oprandnum2=int(self.oprandtext)
            else:
                self.oprandnum2=float(self.oprandtext)
            oprator=self.oprator
            print('oprator={}'.format(self.oprator))
            print('oprand1={}'.format(self.oprandnum1))
            print('oprand2={}'.format(self.oprandnum2))
            if oprator == '+':
                self.result=self.oprandnum1+self.oprandnum2
            elif oprator == '-':
                self.result=self.oprandnum1-self.oprandnum2
            elif oprator == '*':
                self.result=self.oprandnum1*self.oprandnum2
            else:# oprator == '/'
                if self.oprandnum2 != 0:
                    self.result=self.oprandnum1/self.oprandnum2
                else:
                    self.result='MATH ERROR'

            self.decimal=self.comboBox.currentIndex()
            print('decimal places:{}'.format(self.decimal))
            if self.result != 'MATH ERROR':
                if self.decimal == 0:
                    self.result=int(self.result)
                elif self.decimal ==1:
                    self.result=format(self.result,'.1f')
                elif self.decimal ==2:
                    self.result=format(self.result,'.2f')
                elif self.decimal ==3:
                    self.result=format(self.result,'.3f')
                elif self.decimal ==4:
                    self.result=format(self.result,'.4f')
                elif self.decimal ==5:
                    self.result=format(self.result,'.5f')
            if self.checkBox.checkState():
                resultstring='{0:,}'.format(self.result)
            else:
                resultstring=str(self.result)
            self.lineEdit.setText(resultstring[0:11])
            self.equalflag=1
            self.oprator=""
            self.oprandnum1=float(self.result)
            self.oprandnum2=0
            self.oprandtext=""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
# Run the main Qt loop
    app.exec_()
