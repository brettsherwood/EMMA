from PyQt5 import QtCore, QtGui, QtWidgets
from RecycleSymbolDialog import RecycleSymbolDialog
from GlassRinseDialog import GlassRinseDialog
from PaperSelectDialog import PaperSelectDialog
from AluminumRinseDialog import AluminumRinseDialog

class MaterialSelectDialog(object):
    def setupMaterialSelect(self, Dialog):
        #Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Select Material")

        #Material Select Label
        self.lbl_materialSelect = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_materialSelect.sizePolicy().hasHeightForWidth())
        self.lbl_materialSelect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_materialSelect.setFont(font)
        self.lbl_materialSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_materialSelect.setWordWrap(True)
        self.lbl_materialSelect.setObjectName("lbl_materialSelect")
        self.gridLayout.addWidget(self.lbl_materialSelect, 0, 0, 1, 3)
        self.lbl_materialSelect.setText("Please select the material your item is made of:")

        #Paper Button
        self.btn_paper = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_paper.sizePolicy().hasHeightForWidth())
        self.btn_paper.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_paper.setFont(font)
        self.btn_paper.setObjectName("btn_paper")
        self.gridLayout.addWidget(self.btn_paper, 1, 0, 1, 1)
        self.btn_paper.setText("Paper")
        self.btn_paper.clicked.connect(self.openPaperSelectDialog)
        self.btn_paper.clicked.connect(Dialog.close)

        #Plastic Button
        self.btn_plastic = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plastic.sizePolicy().hasHeightForWidth())
        self.btn_plastic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_plastic.setFont(font)        
        self.btn_plastic.setObjectName("btn_plastic")
        self.gridLayout.addWidget(self.btn_plastic, 1, 1, 1, 1)
        self.btn_plastic.setText("Plastic")
        self.btn_plastic.clicked.connect(self.openRecycleSymbolDialog)
        self.btn_plastic.clicked.connect(Dialog.close)      #REMEMBER THIS

        #Glass Button
        self.btn_glass = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_glass.sizePolicy().hasHeightForWidth())
        self.btn_glass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_glass.setFont(font)
        self.btn_glass.setObjectName("btn_glass")
        self.gridLayout.addWidget(self.btn_glass, 1, 2, 1, 1)
        self.btn_glass.setText("Glass")
        self.btn_glass.clicked.connect(self.openGlassRinseDialog)
        self.btn_glass.clicked.connect(Dialog.close)

        #Aluminum Button
        self.btn_aluminum = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aluminum.sizePolicy().hasHeightForWidth())
        self.btn_aluminum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_aluminum.setFont(font)
        self.btn_aluminum.setObjectName("btn_aluminum")
        self.gridLayout.addWidget(self.btn_aluminum, 2, 0, 1, 1)
        self.btn_aluminum.setText("Aluminum")
        self.btn_aluminum.clicked.connect(self.openAluminumRinseDialog)
        self.btn_aluminum.clicked.connect(Dialog.close)

        #Other Button
        self.btn_other = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_other.sizePolicy().hasHeightForWidth())
        self.btn_other.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_other.setFont(font)
        self.btn_other.setObjectName("btn_other")
        self.gridLayout.addWidget(self.btn_other, 2, 2, 1, 1)
        self.btn_other.setText("Other")       

        #Cancel Button Box
        self.bb_cancel = QtWidgets.QDialogButtonBox(Dialog)
        self.bb_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.bb_cancel.setCenterButtons(True)
        self.bb_cancel.setObjectName("bb_cancel")
        self.gridLayout.addWidget(self.bb_cancel, 3, 0, 1, 3)
        self.bb_cancel.accepted.connect(Dialog.accept)
        self.bb_cancel.rejected.connect(Dialog.reject)

        #Recycle Emoji Label
        self.lbl_recycleEmoji = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.lbl_recycleEmoji.setFont(font)
        self.lbl_recycleEmoji.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_recycleEmoji.setObjectName("lbl_recycleEmoji")
        self.gridLayout.addWidget(self.lbl_recycleEmoji, 2, 1, 1, 1)
        self.lbl_recycleEmoji.setText("♻️")
        
    def openRecycleSymbolDialog(self):
        self.RecycleSymbol = QtWidgets.QDialog()
        self.ui = RecycleSymbolDialog()
        self.ui.setupRecycleSymbol(self.RecycleSymbol)
        self.RecycleSymbol.show()

    def openGlassRinseDialog(self):
        self.GlassRinse = QtWidgets.QDialog()
        self.ui = GlassRinseDialog()
        self.ui.setupGlassRinse(self.GlassRinse)
        self.GlassRinse.show()

    def openPaperSelectDialog(self):
        self.PaperSelect = QtWidgets.QDialog()
        self.ui = PaperSelectDialog()
        self.ui.setupPaperSelect(self.PaperSelect)
        self.PaperSelect.show()

    def openAluminumRinseDialog(self):
        self.AluminumRinse = QtWidgets.QDialog()
        self.ui = AluminumRinseDialog()
        self.ui.setupAluminumRinse(self.AluminumRinse)
        self.AluminumRinse.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MaterialSelectDialog()
    ui.setupMaterialSelect(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

