from PyQt5 import QtCore, QtGui, QtWidgets
from YesPlasticBagDialog import YesPlasticBagDialog
from NoPlasticBagDialog import NoPlasticBagDialog

class RecycleSymbolDialog(object):
    def setupRecycleSymbol(self, Dialog):
        #Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Is Recycle Symbol Present?")

        #Symbol Label
        self.lbl_symbolPresent = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_symbolPresent.setFont(font)
        self.lbl_symbolPresent.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_symbolPresent.setWordWrap(True)
        self.lbl_symbolPresent.setObjectName("lbl_symbolPresent")
        self.gridLayout.addWidget(self.lbl_symbolPresent, 0, 0, 1, 2)
        self.lbl_symbolPresent.setText("Is the recycle symbol (♻️) present on"
                                       " your item?")

        #Yes Button
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
        self.btn_yes.clicked.connect(self.openYesPlasticBagDialog)
        self.btn_yes.clicked.connect(Dialog.close)

        #No Button
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
        self.btn_no.clicked.connect(self.openNoPlasticBagDialog)
        self.btn_no.clicked.connect(Dialog.close)

        #Cancel Button Box
        self.bb_cancel = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bb_cancel.sizePolicy().hasHeightForWidth())
        self.bb_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bb_cancel.setFont(font)
        self.bb_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.bb_cancel.setCenterButtons(True)
        self.bb_cancel.setObjectName("bb_cancel")
        self.gridLayout.addWidget(self.bb_cancel, 2, 0, 1, 2)
        self.bb_cancel.accepted.connect(Dialog.accept)
        self.bb_cancel.rejected.connect(Dialog.reject)

    def openYesPlasticBagDialog(self):
        self.YesPlasticBag = QtWidgets.QDialog()
        self.ui = YesPlasticBagDialog()
        self.ui.setupYesPlasticBag(self.YesPlasticBag)
        self.YesPlasticBag.show()

    def openNoPlasticBagDialog(self):
        self.NoPlasticBag = QtWidgets.QDialog()
        self.ui = NoPlasticBagDialog()
        self.ui.setupNoPlasticBag(self.NoPlasticBag)
        self.NoPlasticBag.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RecycleSymbolDialog()
    ui.setupRecycleSymbol(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

