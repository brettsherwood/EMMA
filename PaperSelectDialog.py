from PyQt5 import QtCore, QtGui, QtWidgets
from PaperTrashDialog import PaperTrashDialog
from TrashDialog import TrashDialog
from PaperFoodDialog import PaperFoodDialog
from WetPaperDialog import WetPaperDialog

class PaperSelectDialog(object):
    def setupPaperSelect(self, Dialog):
        #Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Select Paper Type")

        #Paper Select Label
        self.lbl_paperSelect = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_paperSelect.setFont(font)
        self.lbl_paperSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_paperSelect.setWordWrap(True)
        self.lbl_paperSelect.setObjectName("lbl_paperSelect")
        self.gridLayout.addWidget(self.lbl_paperSelect, 0, 0, 1, 3)
        self.lbl_paperSelect.setText("What type of paper is your item made of?")
        
        #Printer/Notebook Button
        self.btn_regular = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_regular.sizePolicy().hasHeightForWidth())
        self.btn_regular.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_regular.setFont(font)
        self.btn_regular.setObjectName("btn_regular")
        self.gridLayout.addWidget(self.btn_regular, 1, 0, 1, 1)
        self.btn_regular.setText("Printer/Notebook")
        self.btn_regular.clicked.connect(self.openWetPaperDialog)
        self.btn_regular.clicked.connect(Dialog.close)

        #Newspaper Button
        self.btn_newspaper = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_newspaper.sizePolicy().hasHeightForWidth())
        self.btn_newspaper.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_newspaper.setFont(font)
        self.btn_newspaper.setObjectName("btn_newspaper")
        self.gridLayout.addWidget(self.btn_newspaper, 1, 1, 1, 1)
        self.btn_newspaper.setText("Newspaper")
        self.btn_newspaper.clicked.connect(self.openWetPaperDialog)
        self.btn_newspaper.clicked.connect(Dialog.close)
        
        #Cardboard Button
        self.btn_cardboard = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cardboard.sizePolicy().hasHeightForWidth())
        self.btn_cardboard.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cardboard.setFont(font)
        self.btn_cardboard.setObjectName("btn_cardboard")
        self.gridLayout.addWidget(self.btn_cardboard, 1, 2, 1, 1)
        self.btn_cardboard.setText("Cardboard")
        self.btn_cardboard.clicked.connect(self.openPaperFoodDialog)
        self.btn_cardboard.clicked.connect(Dialog.close)

        #Coffee Cup Button
        self.btn_coffee = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_coffee.sizePolicy().hasHeightForWidth())
        self.btn_coffee.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_coffee.setFont(font)
        self.btn_coffee.setObjectName("btn_coffee")
        self.gridLayout.addWidget(self.btn_coffee, 2, 0, 1, 1)
        self.btn_coffee.setText("Coffee Cup")
        self.btn_coffee.clicked.connect(self.openTrashDialog)
        self.btn_coffee.clicked.connect(Dialog.close)
        
        #None Button
        self.btn_none = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_none.sizePolicy().hasHeightForWidth())
        self.btn_none.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_none.setFont(font)
        self.btn_none.setObjectName("btn_none")
        self.gridLayout.addWidget(self.btn_none, 2, 1, 1, 2)
        self.btn_none.setText("None of these.")
        self.btn_none.clicked.connect(self.openPaperTrashDialog)
        self.btn_none.clicked.connect(Dialog.close)

        #Cancel Button Box
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

    def openPaperTrashDialog(self):
        self.PaperTrash = QtWidgets.QDialog()
        self.ui = PaperTrashDialog()
        self.ui.setupPaperTrash(self.PaperTrash)
        self.PaperTrash.show()

    def openTrashDialog(self):
        self.Trash = QtWidgets.QDialog()
        self.ui = TrashDialog()
        self.ui.setupTrash(self.Trash)
        self.Trash.show()

    def openPaperFoodDialog(self):
        self.Food = QtWidgets.QDialog()
        self.ui = PaperFoodDialog()
        self.ui.setupPaperFood(self.Food)
        self.Food.show()

    def openWetPaperDialog(self):
        self.WetPaper = QtWidgets.QDialog()
        self.ui = WetPaperDialog()
        self.ui.setupWetPaper(self.WetPaper)
        self.WetPaper.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PaperSelectDialog()
    ui.setupPaperSelect(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

