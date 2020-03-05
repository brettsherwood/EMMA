from PyQt5 import QtCore, QtGui, QtWidgets

class ScannedDialog(object):
    # Creates Scanned Dialog
    def setupScanned(self, Scanned, Material, Recycle, Rinse):
        # Dialog Window
        Scanned.setObjectName("Scanned")
        Scanned.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Scanned)
        self.verticalLayout.setObjectName("verticalLayout")
        Scanned.setWindowTitle("Scanned")

        # Material Label
        self.lbl_material = QtWidgets.QLabel(Scanned)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_material.setFont(font)
        self.lbl_material.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_material.setObjectName("lbl_material")
        self.verticalLayout.addWidget(self.lbl_material)
        self.lbl_material.setText(Material)

        # Recycle Label
        self.lbl_recycle = QtWidgets.QLabel(Scanned)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_recycle.setFont(font)
        self.lbl_recycle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_recycle.setObjectName("lbl_recycle")
        self.verticalLayout.addWidget(self.lbl_recycle)
        self.lbl_recycle.setText(Recycle)

        # Rinse Label
        self.lbl_rinse = QtWidgets.QLabel(Scanned)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_rinse.setFont(font)
        self.lbl_rinse.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rinse.setObjectName("lbl_rinse")
        self.verticalLayout.addWidget(self.lbl_rinse)
        self.lbl_rinse.setText(Rinse)

        # Close Dialog Button
        self.btn_close = QtWidgets.QDialogButtonBox(Scanned)
        self.btn_close.setOrientation(QtCore.Qt.Horizontal)
        self.btn_close.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.btn_close.setCenterButtons(True)
        self.btn_close.setObjectName("btn_close")
        self.verticalLayout.addWidget(self.btn_close)
        self.btn_close.accepted.connect(Scanned.accept)
        self.btn_close.rejected.connect(Scanned.reject)

        
# Only needed to test window on its own
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Scanned = QtWidgets.QDialog()
    ui = ScannedDialog()
    ui.setupScanned(Scanned,'Material', 'Recycle', 'Rinse')
    Scanned.show()
    sys.exit(app.exec_())
      

