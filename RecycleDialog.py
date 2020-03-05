from PyQt5 import QtCore, QtGui, QtWidgets

class RecycleDialog(object):
    def setupRecycle(self, Dialog):
        # Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Thank you for recycling!")

        # Recycle Label
        self.lbl_recycle = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_recycle.setFont(font)
        self.lbl_recycle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_recycle.setWordWrap(True)
        self.lbl_recycle.setObjectName("lbl_recycle")
        self.gridLayout.addWidget(self.lbl_recycle, 0, 0, 1, 1)
        self.lbl_recycle.setText("Your item is ready to be recycled! Please"
                                 " place your item in the correct bin."
                                 " Thank you for recycling!")
        
        # Okay Button Box
        self.bb_okay = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bb_okay.setFont(font)
        self.bb_okay.setOrientation(QtCore.Qt.Horizontal)
        self.bb_okay.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.bb_okay.setCenterButtons(True)
        self.bb_okay.setObjectName("bb_okay")
        self.gridLayout.addWidget(self.bb_okay, 1, 0, 1, 1)
        self.bb_okay.accepted.connect(Dialog.accept)
        self.bb_okay.rejected.connect(Dialog.reject)
        
# Needed to run window by itself
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RecycleDialog()
    ui.setupRecycle(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

