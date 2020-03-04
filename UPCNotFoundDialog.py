from PyQt5 import QtCore, QtGui, QtWidgets
from AddItemDialog import AddItemDialog

class UPCNotFoundDialog(object):
    def setupNotFound(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        #Not Found Label
        self.lbl_notFound = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lbl_notFound.setFont(font)
        self.lbl_notFound.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_notFound.setObjectName("lbl_notFound")
        self.verticalLayout.addWidget(self.lbl_notFound)

        #Add Item Label
        self.lbl_addItem = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_addItem.setFont(font)
        self.lbl_addItem.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_addItem.setObjectName("lbl_addItem")
        self.verticalLayout.addWidget(self.lbl_addItem)

        #Dialog Button Box
        self.btn_yes_no = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_yes_no.setOrientation(QtCore.Qt.Horizontal)
        self.btn_yes_no.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btn_yes_no.setCenterButtons(True)
        self.btn_yes_no.setObjectName("btn_yes_no")
        self.verticalLayout.addWidget(self.btn_yes_no)

        self.retranslateUi(Dialog)
        self.btn_yes_no.accepted.connect(self.addNewItem)
        self.btn_yes_no.accepted.connect(Dialog.accept)
        self.btn_yes_no.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UPC Not Found"))
        self.lbl_notFound.setText(_translate("Dialog", "UPC Not Found"))
        self.lbl_addItem.setText(_translate("Dialog", "Would you like to add this item to the database?"))

    def addNewItem(self):       #opens NewItem Window when Yes is selected
        self.addItem = QtWidgets.QDialog()
        self.ui = AddItemDialog()
        self.ui.setupAddItem(self.addItem)
        self.addItem.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UPCNotFoundDialog()
    ui.setupNotFound(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

