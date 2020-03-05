from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PlasticRinseDialog import PlasticRinseDialog
from RecycleDialog import RecycleDialog
from ServoFuncs import openLid
from Worker import Worker

class PlasticFoodLiquidDialog(object):
    def setupPlasticFoodLiquid(self, Dialog):
        # Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Food or Liquid?")

        # Food or Liquid Label
        self.lbl_foodliquid = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_foodliquid.setFont(font)
        self.lbl_foodliquid.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_foodliquid.setWordWrap(True)
        self.lbl_foodliquid.setObjectName("lbl_foodliquid")
        self.gridLayout.addWidget(self.lbl_foodliquid, 0, 0, 1, 2)
        self.lbl_foodliquid.setText("Did your item contain food or liquid?")

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
        self.gridLayout.addWidget(self.btn_yes, 2, 0, 1, 1)
        self.btn_yes.setText("Yes")
        self.btn_yes.clicked.connect(self.openPlasticRinseDialog)
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
        self.gridLayout.addWidget(self.btn_no, 2, 1, 1, 1)
        self.btn_no.setText("No")
        self.btn_no.clicked.connect(self.openRecycleDialog)
        self.btn_no.clicked.connect(Dialog.close)
        # OPEN PLASTIC LID HERE
        self.btn_no.clicked.connect(self.openPlasticLid)
        self.threadpool = QThreadPool()

        # Cancel Button Box
        self.bb_cancel = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bb_cancel.setFont(font)
        self.bb_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.bb_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.bb_cancel.setCenterButtons(True)
        self.bb_cancel.setObjectName("bb_cancel")
        self.gridLayout.addWidget(self.bb_cancel, 3, 0, 1, 2)
        self.bb_cancel.accepted.connect(Dialog.accept)
        self.bb_cancel.rejected.connect(Dialog.reject)

    def openPlasticRinseDialog(self):
        self.PlasticRinse = QtWidgets.QDialog()
        self.ui = PlasticRinseDialog()
        self.ui.setupPlasticRinse(self.PlasticRinse)
        self.PlasticRinse.show()

    def openRecycleDialog(self):
        self.Recycle = QtWidgets.QDialog()
        self.ui = RecycleDialog()
        self.ui.setupRecycle(self.Recycle)
        self.Recycle.show()

    def openPlasticLid(self):
        # Pass the function to execute
        worker = Worker(lambda: openLid(0))
        #  Execute
        self.threadpool.start(worker)
        
# Needed to run window by itself
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PlasticFoodLiquidDialog()
    ui.setupPlasticFoodLiquid(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

