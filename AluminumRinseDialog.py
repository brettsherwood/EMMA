from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from RecycleDialog import RecycleDialog
from ServoFuncs import openLid
from Worker import Worker

class AluminumRinseDialog(object):
    def setupAluminumRinse(self, Dialog):
        # Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Please Rinse your Item")

        # Rinse Label
        self.lbl_rinse = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_rinse.setFont(font)
        self.lbl_rinse.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rinse.setWordWrap(True)
        self.lbl_rinse.setObjectName("lbl_rinse")
        self.gridLayout.addWidget(self.lbl_rinse, 0, 0, 1, 1)
        self.lbl_rinse.setText("Please rinse your item out to avoid"
                               " getting the other recyclables dirty."
                               " Then you may recycle your item.")

        # Rinse Button
        self.btn_rinse = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_rinse.setFont(font)
        self.btn_rinse.setObjectName("btn_rinse")
        self.gridLayout.addWidget(self.btn_rinse, 1, 0, 1, 1)
        self.btn_rinse.setText("My item has been rinsed.")
        self.btn_rinse.clicked.connect(self.openRecycleDialog)
        self.btn_rinse.clicked.connect(Dialog.close)
        # OPEN ALUMINUM LID HERE
        self.btn_rinse.clicked.connect(self.openAluminumLid)
        self.threadpool = QThreadPool()
        
    def openRecycleDialog(self):
        self.Recycle = QtWidgets.QDialog()
        self.ui = RecycleDialog()
        self.ui.setupRecycle(self.Recycle)
        self.Recycle.show()
        
    def openAluminumLid(self):
        # Pass the function to execute
        worker = Worker(lambda: openLid(3))
        # Execute
        self.threadpool.start(worker)
    
# Used to test window by itself
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AluminumRinseDialog()
    ui.setupAluminumRinse(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

