from PyQt5 import QtCore, QtGui, QtWidgets

class InvalidItemDialog(object):
    def setupInvalidItemDialog(self, Dialog):
        # Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Invalid Item")

        # Invalid item Label
        self.lbl_Invalid = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Invalid.setFont(font)
        self.lbl_Invalid.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Invalid.setWordWrap(True)
        self.lbl_Invalid.setObjectName("lbl_Invalid")
        self.gridLayout.addWidget(self.lbl_Invalid, 0, 0, 1, 1)
        self.lbl_Invalid.setText("Invalid item entry. Please make sure all "
                                 "fields are filled and that you tap inside the "
                                 "barcode field before you scan the item.")

        # OK Button Box
        self.bb_okay = QtWidgets.QDialogButtonBox(Dialog)
        self.bb_okay.setOrientation(QtCore.Qt.Horizontal)
        self.bb_okay.setStandardButtons(QtWidgets.QDialogButtonBox.Retry)
        self.bb_okay.setCenterButtons(True)
        self.bb_okay.setObjectName("bb_okay")
        self.gridLayout.addWidget(self.bb_okay, 1, 0, 1, 1)
        self.bb_okay.accepted.connect(Dialog.accept)
        self.bb_okay.rejected.connect(Dialog.reject)

# Needed to test window by itself
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = InvalidItemDialog()
    ui.setupInvalidItemDialog(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
