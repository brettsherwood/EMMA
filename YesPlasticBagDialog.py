from PyQt5 import QtCore, QtGui, QtWidgets
from PlasticBagRecycleDialog import PlasticBagRecycleDialog
from PlasticNumberDialog import PlasticNumberDialog

class YesPlasticBagDialog(object):
    def setupYesPlasticBag(self, Dialog):
        # Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Plastic Bag?")

        # Plastic Bag Label
        self.lbl_plasticbag = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_plasticbag.setFont(font)
        self.lbl_plasticbag.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_plasticbag.setWordWrap(True)
        self.lbl_plasticbag.setObjectName("lbl_plasticbag")
        self.gridLayout.addWidget(self.lbl_plasticbag, 0, 0, 1, 2)
        self.lbl_plasticbag.setText("Is your item a plastic bag?")

        # Yes Button
        self.btn_yes = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_yes.sizePolicy().hasHeightForWidth())
        self.btn_yes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_yes.setFont(font)
        self.btn_yes.setObjectName("btn_yes")
        self.gridLayout.addWidget(self.btn_yes, 1, 0, 1, 1)
        self.btn_yes.setText("Yes")
        self.btn_yes.clicked.connect(self.openPlasticBagRecycleDialog)
        self.btn_yes.clicked.connect(Dialog.close)

        # No Button
        self.btn_no = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_no.sizePolicy().hasHeightForWidth())
        self.btn_no.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_no.setFont(font)
        self.btn_no.setObjectName("btn_no")
        self.gridLayout.addWidget(self.btn_no, 1, 1, 1, 1)
        self.btn_no.setText("No")
        self.btn_no.clicked.connect(self.openPlasticNumberDialog)
        self.btn_no.clicked.connect(Dialog.close)

        # Cancel Button Box
        self.bb_cancel = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bb_cancel.setFont(font)
        self.bb_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.bb_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.bb_cancel.setCenterButtons(True)
        self.bb_cancel.setObjectName("bb_cancel")
        self.gridLayout.addWidget(self.bb_cancel, 2, 0, 1, 2)
        self.bb_cancel.accepted.connect(Dialog.accept)
        self.bb_cancel.rejected.connect(Dialog.reject)

    def openPlasticBagRecycleDialog(self):
        self.PlasticBagRecycle = QtWidgets.QDialog()
        self.ui = PlasticBagRecycleDialog()
        self.ui.setupPlasticBagRecycle(self.PlasticBagRecycle)
        self.PlasticBagRecycle.show()

    def openPlasticNumberDialog(self):
        self.PlasticNumber = QtWidgets.QDialog()
        self.ui = PlasticNumberDialog()
        self.ui.setupPlasticNumber(self.PlasticNumber)
        self.PlasticNumber.show()

# Needed to test window by itself
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = YesPlasticBagDialog()
    ui.setupYesPlasticBag(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

