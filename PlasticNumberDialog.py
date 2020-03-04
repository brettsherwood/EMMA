from PyQt5 import QtCore, QtGui, QtWidgets
from TrashDialog import TrashDialog
from PlasticFoodLiquidDialog import PlasticFoodLiquidDialog

class PlasticNumberDialog(object):
    def setupPlasticNumber(self, Dialog):
        #Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Select Plastic Number")

        #Select Label
        self.lbl_select = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_select.sizePolicy().hasHeightForWidth())
        self.lbl_select.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_select.setFont(font)
        self.lbl_select.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_select.setWordWrap(True)
        self.lbl_select.setObjectName("lbl_select")
        self.gridLayout.addWidget(self.lbl_select, 0, 1, 1, 3)
        self.lbl_select.setText("Please select the number inside of the ♻️"
                                " symbol on your plastic item. This is usually"
                                " located on the bottom.")
        
        #Button 1
        self.btn_1 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 1, 1, 1, 1)
        self.btn_1.setText("1")
        self.btn_1.clicked.connect(self.openPlasticFoodLiquidDialog)
        self.btn_1.clicked.connect(Dialog.close)
        
        #Button 2
        self.btn_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 1, 2, 1, 1)
        self.btn_2.setText("2")
        self.btn_2.clicked.connect(self.openPlasticFoodLiquidDialog)
        self.btn_2.clicked.connect(Dialog.close)
        
        #Button 3
        self.btn_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 1, 3, 1, 1)
        self.btn_3.setText("3")
        self.btn_3.clicked.connect(self.openPlasticFoodLiquidDialog)
        self.btn_3.clicked.connect(Dialog.close)
        
        #Button 4
        self.btn_4 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 1, 1, 1)
        self.btn_4.setText("4")
        self.btn_4.clicked.connect(self.openPlasticFoodLiquidDialog)
        self.btn_4.clicked.connect(Dialog.close)
        
        #Button 5
        self.btn_5 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 2, 1, 1)
        self.btn_5.setText("5")
        self.btn_5.clicked.connect(self.openPlasticFoodLiquidDialog)
        self.btn_5.clicked.connect(Dialog.close)

        #Button 6
        self.btn_6 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 3, 1, 1)
        self.btn_6.setText("6")
        self.btn_6.clicked.connect(self.openTrashDialog)
        self.btn_6.clicked.connect(Dialog.close)

        #Button 7
        self.btn_7 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 3, 1, 1, 1)
        self.btn_7.setText("7")
        self.btn_7.clicked.connect(self.openPlasticFoodLiquidDialog)
        self.btn_7.clicked.connect(Dialog.close)

        #Cancel Button Box
        self.bb_cancel = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bb_cancel.sizePolicy().hasHeightForWidth())
        self.bb_cancel.setSizePolicy(sizePolicy)
        self.bb_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.bb_cancel.setCenterButtons(True)
        self.bb_cancel.setObjectName("bb_cancel")
        self.gridLayout.addWidget(self.bb_cancel, 3, 2, 1, 2)
        self.bb_cancel.accepted.connect(Dialog.accept)
        self.bb_cancel.rejected.connect(Dialog.reject)

    def openTrashDialog(self):
        self.Trash = QtWidgets.QDialog()
        self.ui = TrashDialog()
        self.ui.setupTrash(self.Trash)
        self.Trash.show()

    def openPlasticFoodLiquidDialog(self):
        self.PlasticFoodLiquid = QtWidgets.QDialog()
        self.ui = PlasticFoodLiquidDialog()
        self.ui.setupPlasticFoodLiquid(self.PlasticFoodLiquid)
        self.PlasticFoodLiquid.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PlasticNumberDialog()
    ui.setupPlasticNumber(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

