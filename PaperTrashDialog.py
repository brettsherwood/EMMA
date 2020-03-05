from PyQt5 import QtCore, QtGui, QtWidgets

class PaperTrashDialog(object):
    def setupPaperTrash(self, Dialog):
        # Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Please throw away.")
        
        # Trash Label
        self.lbl_trash = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_trash.setFont(font)
        self.lbl_trash.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_trash.setWordWrap(True)
        self.lbl_trash.setObjectName("lbl_trash")
        self.gridLayout.addWidget(self.lbl_trash, 0, 0, 1, 1)
        self.lbl_trash.setText("Items such as Paper Towels, Napkins, "
                               "Tissues, or Sticky Notes, are not "
                               "recyclable. Please throw them away.")
        
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
    ui = PaperTrashDialog()
    ui.setupPaperTrash(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

