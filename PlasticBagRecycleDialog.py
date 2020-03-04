from PyQt5 import QtCore, QtGui, QtWidgets

class PlasticBagRecycleDialog(object):
    def setupPlasticBagRecycle(self, Dialog):
        #Main Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        Dialog.setWindowTitle("Please Recycle Your Plastic Bag")

        #Recycle Plastic Bag Label        
        self.lbl_recyclePlasticBag = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_recyclePlasticBag.setFont(font)
        self.lbl_recyclePlasticBag.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_recyclePlasticBag.setWordWrap(True)
        self.lbl_recyclePlasticBag.setObjectName("lbl_recyclePlasticBag")
        self.gridLayout.addWidget(self.lbl_recyclePlasticBag, 0, 0, 1, 1)
        self.lbl_recyclePlasticBag.setText("Please place your plastic bag in"
                                           " the plastic bag on the wall to be"
                                           " recycled.")
        #Okay Button Box
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PlasticBagRecycleDialog()
    ui.setupPlasticBagRecycle(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

