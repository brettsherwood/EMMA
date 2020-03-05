from PyQt5 import QtCore, QtGui, QtWidgets
from InvalidItemDialog import InvalidItemDialog
import csv

class AddItemDialog(object):
    def setupAddItem(self, Dialog):
        #Main Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        #Material Label
        self.lbl_material = QtWidgets.QLabel(Dialog)
        self.lbl_material.setObjectName("lbl_material")
        self.gridLayout.addWidget(self.lbl_material, 0, 0, 1, 1)

        #Material Combo Box
        self.cb_material = QtWidgets.QComboBox(Dialog)
        self.cb_material.setObjectName("cb_material")
        self.gridLayout.addWidget(self.cb_material, 0, 1, 1, 1)
        material_list = ['', 'Paper', 'Plastic', 'Glass', 'Aluminum', 'Other']
        self.cb_material.addItems(material_list)

        #Recycle Label
        self.lbl_recycle = QtWidgets.QLabel(Dialog)
        self.lbl_recycle.setObjectName("lbl_recycle")
        self.gridLayout.addWidget(self.lbl_recycle, 1, 0, 1, 1)

        #Recycle Combo Box
        self.cb_recycle = QtWidgets.QComboBox(Dialog)
        self.cb_recycle.setObjectName("cb_recycle")
        self.gridLayout.addWidget(self.cb_recycle, 1, 1, 1, 1)
        recycle_list = ['', 'Yes', 'No']
        self.cb_recycle.addItems(recycle_list)

        #Rinse Label
        self.lbl_rinse = QtWidgets.QLabel(Dialog)
        self.lbl_rinse.setObjectName("lbl_rinse")
        self.gridLayout.addWidget(self.lbl_rinse, 2, 0, 1, 1)

        #Rinse Combo Box
        self.cb_rinse = QtWidgets.QComboBox(Dialog)
        self.cb_rinse.setObjectName("cb_rinse")
        self.gridLayout.addWidget(self.cb_rinse, 2, 1, 1, 1)
        rinse_list = ['', 'Yes', 'No']
        self.cb_rinse.addItems(rinse_list)

        #Barcode Label
        self.lbl_barcode = QtWidgets.QLabel(Dialog)
        self.lbl_barcode.setObjectName("lbl_barcode")
        self.gridLayout.addWidget(self.lbl_barcode, 3, 0, 1, 1)

        #Barcode Line Edit
        self.le_barcode = QtWidgets.QLineEdit(Dialog)
        self.le_barcode.setObjectName("le_barcode")
        self.gridLayout.addWidget(self.le_barcode, 3, 1, 1, 1)

        #Button Box
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.checkInput)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def checkInput(self):
        upc = self.le_barcode.text()                #takes current selections from comboboxes
        material = self.cb_material.currentText()   #to create variables to add to database
        recycle = self.cb_recycle.currentText()
        rinse = self.cb_rinse.currentText()

        if (upc == '' or material == '' or recycle == '' or rinse == ''):
            self.openInvalidItemDialog()
        else:
            self.newItem(upc, material, recycle, rinse)
            self.Dialog.close()
            
    def newItem(self, upc, material, recycle, rinse):
        APPENDFILE = open('UPCList.csv', 'a')       #opens file to append new entry
        entryWriter = csv.writer(APPENDFILE, lineterminator = '\n')
        entryWriter.writerow([upc, material, recycle, rinse])   #writes new item into database
        APPENDFILE.close()      #closes file to not cause errors

            
    def openInvalidItemDialog(self):
        self.Invalid = QtWidgets.QDialog()
        self.ui = InvalidItemDialog()
        self.ui.setupInvalidItemDialog(self.Invalid)
        self.Invalid.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Item"))
        self.lbl_material.setText(_translate("Dialog", "Item's Material:"))
        self.lbl_recycle.setText(_translate("Dialog", "Is it Recyclable?:"))
        self.lbl_rinse.setText(_translate("Dialog", "Does it need to be Rinsed?:"))
        self.lbl_barcode.setText(_translate("Dialog", "Click box and Scan Barcode:"))

#only needed to run window by itself
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AddItemDialog()
    ui.setupAddItem(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

