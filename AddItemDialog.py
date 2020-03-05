from PyQt5 import QtCore, QtGui, QtWidgets
from InvalidItemDialog import InvalidItemDialog
import csv

class AddItemDialog(object):
    def setupAddItem(self, Dialog):
        # Main Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Add Item")
        
        # Material Label
        self.lbl_material = QtWidgets.QLabel(Dialog)
        self.lbl_material.setObjectName("lbl_material")
        self.gridLayout.addWidget(self.lbl_material, 0, 0, 1, 1)
        self.lbl_material.setText("Item's Material:")

        # Material Combo Box
        self.cb_material = QtWidgets.QComboBox(Dialog)
        self.cb_material.setObjectName("cb_material")
        self.gridLayout.addWidget(self.cb_material, 0, 1, 1, 1)
        material_list = ['', 'Paper', 'Plastic', 'Glass', 'Aluminum', 'Other']
        self.cb_material.addItems(material_list)

        # Recycle Label
        self.lbl_recycle = QtWidgets.QLabel(Dialog)
        self.lbl_recycle.setObjectName("lbl_recycle")
        self.gridLayout.addWidget(self.lbl_recycle, 1, 0, 1, 1)
        self.lbl_recycle.setText("Is it Recyclable?:")

        # Recycle Combo Box
        self.cb_recycle = QtWidgets.QComboBox(Dialog)
        self.cb_recycle.setObjectName("cb_recycle")
        self.gridLayout.addWidget(self.cb_recycle, 1, 1, 1, 1)
        recycle_list = ['', 'Yes', 'No']
        self.cb_recycle.addItems(recycle_list)

        # Rinse Label
        self.lbl_rinse = QtWidgets.QLabel(Dialog)
        self.lbl_rinse.setObjectName("lbl_rinse")
        self.gridLayout.addWidget(self.lbl_rinse, 2, 0, 1, 1)
        self.lbl_rinse.setText("Does it need to be Rinsed?:")

        # Rinse Combo Box
        self.cb_rinse = QtWidgets.QComboBox(Dialog)
        self.cb_rinse.setObjectName("cb_rinse")
        self.gridLayout.addWidget(self.cb_rinse, 2, 1, 1, 1)
        rinse_list = ['', 'Yes', 'No']
        self.cb_rinse.addItems(rinse_list)

        # Barcode Label
        self.lbl_barcode = QtWidgets.QLabel(Dialog)
        self.lbl_barcode.setObjectName("lbl_barcode")
        self.gridLayout.addWidget(self.lbl_barcode, 3, 0, 1, 1)
        self.lbl_barcode.setText("Click box and Scan Barcode:")

        # Barcode Line Edit
        self.le_barcode = QtWidgets.QLineEdit(Dialog)
        self.le_barcode.setObjectName("le_barcode")
        self.gridLayout.addWidget(self.le_barcode, 3, 1, 1, 1)

        # Save Button Box
        self.bb_save = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bb_save.setFont(font)
        self.bb_save.setOrientation(QtCore.Qt.Horizontal)
        self.bb_save.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.bb_save.setCenterButtons(True)
        self.bb_save.setObjectName("bb_save")
        self.gridLayout.addWidget(self.bb_save, 4, 0, 1, 2)
        self.bb_save.accepted.connect(self.checkInput)
        self.bb_save.accepted.connect(Dialog.accept)
        self.bb_save.rejected.connect(Dialog.reject)

    # takes current selections from comboboxes to create variables to add to database
    def checkInput(self):
        upc = self.le_barcode.text()                
        material = self.cb_material.currentText()   
        recycle = self.cb_recycle.currentText()
        rinse = self.cb_rinse.currentText()

        if (upc == '' or material == '' or recycle == '' or rinse == ''):
            self.openInvalidItemDialog()
        else:
            self.newItem(upc, material, recycle, rinse)
                 
    def newItem(self, upc, material, recycle, rinse):
        APPENDFILE = open('UPCList.csv', 'a')       # opens file to append new entry
        entryWriter = csv.writer(APPENDFILE, lineterminator = '\n')
        entryWriter.writerow([upc, material, recycle, rinse])   # writes new item into database
        APPENDFILE.close()      # closes file to not cause errors
           
    def openInvalidItemDialog(self):
        self.Invalid = QtWidgets.QDialog()
        self.ui = InvalidItemDialog()
        self.ui.setupInvalidItemDialog(self.Invalid)
        self.Invalid.show()

# only needed to run window by itself
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AddItemDialog()
    ui.setupAddItem(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

