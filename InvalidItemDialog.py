from PyQt5 import QtCore, QtGui, QtWidgets

class InvalidItemDialog(object):
    def setupInvalidItemDialog(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.bb_okay = QtWidgets.QDialogButtonBox(Dialog)
        self.bb_okay.setOrientation(QtCore.Qt.Horizontal)
        self.bb_okay.setStandardButtons(QtWidgets.QDialogButtonBox.Retry)
        self.bb_okay.setCenterButtons(True)
        self.bb_okay.setObjectName("bb_okay")
        self.gridLayout.addWidget(self.bb_okay, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.bb_okay.accepted.connect(Dialog.accept)
        self.bb_okay.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Invalid Item"))
        self.label.setText(_translate("Dialog", "Invalid item entry. Please try again."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = InvalidItemDialog()
    ui.setupInvalidItemDialog(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

