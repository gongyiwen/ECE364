import sys
import re
from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)

        self.btnClear.clicked.connect(self.cleardata)
        self.btnLoad.clicked.connect(self.loadData)
        self.lines=[self.txtZip,self.txtState,self.txtEmail,self.txtLastName,self.txtFirstName,self.txtAddress,self.txtCity]
        for line in self.lines:
            line.textChanged.connect(self.changed)
        self.btnSave.clicked.connect(self.validation)

    def validation(self):
        states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        errormessage=''
        if len(self.txtFirstName.text()) ==0:
            errormessage='Error: FirstName is not valid!'
        if len(self.txtLastName.text())==0:
            errormessage='Error: LastName is not valid!'
        if len(self.txtAddress.text())==0:
            errormessage='Error: Address is not valid!'
        if len(self.txtCity.text())==0:
            errormessage='Error: City is not valid!'
        if not self.txtState.text() in states:
            errormessage='Error: State is not valid!'
        if len(self.txtZip.text())!=5:
            errormessage='Error: Zip is not valid'
        pattern=r"\w+@\w+\.\w+"
        if re.match(pattern,self.txtEmail.text()):
            m=re.match(pattern,self.txtEmail.text())
            if len(m.group(0)) != len(self.txtEmail.text()):
                errormessage='Error: Email is not valid!'
        else:
            errormessage='Error: Email is not valid!'
        self.lblError.setText(errormessage)
        if errormessage == '':
            self.savetofile()

    def savetofile(self):
        line1='<?xml version="1.0" encoding="UTF-8"?>\n'
        line2='<user>\n'
        line3='\t<FirstName>{}</FirstName>\n'.format(self.txtFirstName.text())
        line4='\t<LastName>{}</LastName>\n'.format(self.txtLastName.text())
        line5='\t<Address>{}</Address>\n'.format(self.txtAddress.text())
        line6='\t<City>{}</City>\n'.format(self.txtCity.text())
        line7='\t<State>{}</State>\n'.format(self.txtState.text())
        line8='\t<ZIP>{}</ZIP>\n'.format(self.txtZip.text())
        line9='\t<Email>{}</Email>\n'.format(self.txtEmail.text())
        line10='</user>\n'
        lines=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]
        fp= open('target.xml','w')
        for line in lines:
            fp.write(line)
        fp.close()





    def changed(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)

    def cleardata(self):
        self.txtAddress.clear()
        self.txtCity.clear()
        self.txtEmail.clear()
        self.txtFirstName.clear()
        self.txtLastName.clear()
        self.txtState.clear()
        self.txtZip.clear()
        self.lblError.clear()
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)


    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """
        with open(filePath,'r') as myFile:
            lines=myFile.readlines()
            lines=lines[2:9]
            a=[]
            for line in lines:
                line=line.split('>')[1]
                line=line.split('<')[0]
                a.append(line)
            self.txtFirstName.setText(a[0])
            self.txtLastName.setText(a[1])
            self.txtAddress.setText(a[2])
            self.txtCity.setText(a[3])
            self.txtState.setText(a[4])
            self.txtZip.setText(a[5])
            self.txtEmail.setText(a[6])
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)


        pass

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return
        print(filePath)

        self.loadFromXmlFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
