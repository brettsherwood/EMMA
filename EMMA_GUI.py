from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

# Only imports the class, not the entire module
from ScannedDialog import ScannedDialog
from Database import Database
from UPCNotFoundDialog import UPCNotFoundDialog
from MaterialSelectDialog import MaterialSelectDialog
from TrashDialog import TrashDialog
import ServoFuncs
from Worker import Worker


class EmmaGUI(object):
    # Creates Main Window
    def setupMain(self, main_EMMA):
        # Main Window
        main_EMMA.setObjectName("main_EMMA")
        main_EMMA.resize(800, 400)                              # resizes main window to fit small screen
        self.centralwidget = QtWidgets.QWidget(main_EMMA)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        main_EMMA.setWindowTitle("EMMA")        # title of window when not fullscreen
        main_EMMA.setCentralWidget(self.centralwidget)

        # Barcode LineEdit
        self.le_Barcode = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Barcode.sizePolicy().hasHeightForWidth())
        self.le_Barcode.setSizePolicy(sizePolicy)
        self.le_Barcode.setObjectName("le_Barcode")
        self.gridLayout.addWidget(self.le_Barcode, 2, 3, 1, 1)
        self.le_Barcode.returnPressed.connect(self.scanBarcode) # when enter is pressed, scanBarcode function runs

        # Welcome Label
        self.lbl_Welcome = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Welcome.sizePolicy().hasHeightForWidth())
        self.lbl_Welcome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(40)
        self.lbl_Welcome.setFont(font)
        self.lbl_Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Welcome.setObjectName("lbl_Welcome")
        self.gridLayout.addWidget(self.lbl_Welcome, 1, 0, 1, 4)
        self.lbl_Welcome.setText("Welcome to E.M.M.A.!")

        # Scan Label
        self.lbl_Scan = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Scan.sizePolicy().hasHeightForWidth())
        self.lbl_Scan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lbl_Scan.setFont(font)
        self.lbl_Scan.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Scan.setObjectName("lbl_Scan")
        self.gridLayout.addWidget(self.lbl_Scan, 2, 0, 1, 3)
        self.lbl_Scan.setText("Please Scan Barcode...")

        # Select Label
        self.lbl_Select = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_Select.setFont(font)
        self.lbl_Select.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Select.setWordWrap(True)
        self.lbl_Select.setObjectName("lbl_Select")
        self.gridLayout.addWidget(self.lbl_Select, 3, 0, 1, 4)
        self.lbl_Select.setText("Or, press the button below if your item does not have one.\n"
                                "Please make sure lids are closed before continuing to avoid crashing system.")
        
        # No Barcode Button
        self.btn_NoBarcode = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_NoBarcode.sizePolicy().hasHeightForWidth())
        self.btn_NoBarcode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_NoBarcode.setFont(font)
        self.btn_NoBarcode.setObjectName("btn_NoBarcode")
        self.gridLayout.addWidget(self.btn_NoBarcode, 4, 0, 1, 4)   # row, column, height, width
        self.btn_NoBarcode.setText("Item does not have a barcode")
        self.btn_NoBarcode.clicked.connect(self.openMaterialSelectDialog)

        # Team Label
        self.lbl_Team = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Team.sizePolicy().hasHeightForWidth())
        self.lbl_Team.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Team.setFont(font)
        self.lbl_Team.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Team.setObjectName("lbl_Team")
        self.gridLayout.addWidget(self.lbl_Team, 6, 0, 1, 4)
        self.lbl_Team.setText("♻Clean Green Dream Team in Partner with Waste Management®♻")

        self.threadpool = QThreadPool()
        # QtCore.QMetaObject.connectSlotsByName(main_EMMA)

    def scanBarcode(self):
        self.scan = Database()        
        self.upc = self.le_Barcode.text()
        
        if self.upc != "close":
            self.results = self.scan.scanDatabase(self.upc)
            self.le_Barcode.clear()             # clears barcode from box
            
            if self.results[0] == "Not Found":
                self.openUPCNotFoundDialog()
            else:
                self.material = self.results[0]     # picks apart returned tuple to get variables
                self.recycle = self.results[1][0]
                self.rinse = self.results[1][1]
                if self.material == "Other":
                    self.openTrashDialog()
                else:
                    self.openScannedDialog(self.material, self.recycle, self.rinse)
        else:
            main_EMMA.close()   # enables user to close window when fullscreen

    def openScannedDialog(self, material, recycle, rinse):
        self.Scanned = QtWidgets.QDialog()
        self.ui = ScannedDialog()
        self.Material = ('Material is ' + self.material)
        self.Recycle = ('Item is ' + self.recycle)
        self.Rinse = (self.rinse)
        self.ui.setupScanned(self.Scanned, self.Material, self.Recycle, self.Rinse)
        self.Scanned.show()

        if self.material == "Plastic":
            lidNum = 0
        elif self.material == "Glass":
            lidNum = 1
        elif self.material == "Paper":
            lidNum = 2
        elif self.material == "Aluminum":
            lidNum = 3

        # Pass the function to execute
        worker = Worker(lambda: ServoFuncs.openLid(lidNum))
        # Execute
        self.threadpool.start(worker)  
        
    def openUPCNotFoundDialog(self):
        self.NotFound = QtWidgets.QDialog()
        self.ui = UPCNotFoundDialog()
        self.ui.setupNotFound(self.NotFound)
        self.NotFound.show()

    def openMaterialSelectDialog(self):
        self.MaterialSelect = QtWidgets.QDialog()
        self.ui = MaterialSelectDialog()
        self.ui.setupMaterialSelect(self.MaterialSelect)
        self.MaterialSelect.show()

    def openTrashDialog(self):
        self.Trash = QtWidgets.QDialog()
        self.ui = TrashDialog()
        self.ui.setupTrash(self.Trash)
        self.Trash.show()

if __name__ == "__main__":
    print("Making sure lids are fully closed before starting EMMA.")
    ServoFuncs.closeLids()
    # This is the code the actually starts the GUI
    import sys                  
    app = QtWidgets.QApplication(sys.argv)
    main_EMMA = QtWidgets.QMainWindow()
    ui = EmmaGUI()
    ui.setupMain(main_EMMA)
    main_EMMA.showFullScreen()
    sys.exit(app.exec_())
