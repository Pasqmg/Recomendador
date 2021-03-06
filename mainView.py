from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog, QMessageBox

from datamanager.DataLoader import DataLoader
from views.collaborativeRecommendationWindow import Ui_CollabRecomWindow
from views.dark_custom_pallet import DarkCustomPalette
from views.light_custom_pallet import LightCustomPalette
from views.demographicRecommendationWindow import Ui_DemoRecomWindow
from views.hybridRecommendationWindow import Ui_HybridRecomWindow
from views.newUserWindow import Ui_NewUserWindow
from paths import IMAGE_FOLDER


class Ui_MainWindow(QDialog):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.palette = LightCustomPalette()
        # self.palette = DarkCustomPalette()
        MainWindow.setPalette(self.palette.palette)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 130, 781, 401))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.widget)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.demoButton = QtWidgets.QPushButton(self.frame)
        self.demoButton.setObjectName("demoButton")
        self.verticalLayout.addWidget(self.demoButton)
        self.collabButton = QtWidgets.QPushButton(self.frame)
        self.collabButton.setObjectName("collabButton")
        self.verticalLayout.addWidget(self.collabButton)
        self.hybridButton = QtWidgets.QPushButton(self.frame)
        self.hybridButton.setObjectName("hybridButton")
        self.verticalLayout.addWidget(self.hybridButton)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.newUserButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.newUserButton.setFont(font)
        self.newUserButton.setObjectName("newUserButton")
        self.verticalLayout_2.addWidget(self.newUserButton)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(290, 20, 239, 89))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleLabel = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Keraleeyam")
        font.setPointSize(47)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_3.addWidget(self.titleLabel)
        self.subtitleLabel = QtWidgets.QLabel(self.widget1)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.verticalLayout_3.addWidget(self.subtitleLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.demoButton.clicked.connect(self.demoButton_clicked)
        self.collabButton.clicked.connect(self.collabButton_clicked)
        self.hybridButton.clicked.connect(self.hybridButton_clicked)
        self.newUserButton.clicked.connect(self.newUserButton_clicked)

        self.db = DataLoader()
        self.db.read_all_data()

    def newUserButton_clicked(self):
        self.NewUserWindow = QtWidgets.QMainWindow()
        self.ui = Ui_NewUserWindow(self.db)
        self.ui.setupUi(self.NewUserWindow)
        # MainWindow.hide()
        self.NewUserWindow.show()

    def demoButton_clicked(self):
        self.DemoRecomWindow = QtWidgets.QMainWindow()
        self.ui = Ui_DemoRecomWindow()
        self.ui.setupUi(self.DemoRecomWindow)
        self.DemoRecomWindow.show()

    def collabButton_clicked(self):
        self.CollabRecomWindow = QtWidgets.QMainWindow()
        self.ui = Ui_CollabRecomWindow()
        self.ui.setupUi(self.CollabRecomWindow)
        self.CollabRecomWindow.show()

    def hybridButton_clicked(self):
        self.HybridRecomWindow = QtWidgets.QMainWindow()
        self.ui = Ui_HybridRecomWindow()
        self.ui.setupUi(self.HybridRecomWindow)
        self.HybridRecomWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MovieBinge"))
        self.demoButton.setText(_translate("MainWindow", "Demographic Recommendation"))
        self.collabButton.setText(_translate("MainWindow", "Collaborative Recommendation"))
        self.hybridButton.setText(_translate("MainWindow", "Hybrid Recommendation"))
        self.newUserButton.setText(_translate("MainWindow", "Register new user"))
        self.titleLabel.setText(_translate("MainWindow", "MovieBinge"))
        self.subtitleLabel.setText(_translate("MainWindow", "A movie recommendation system"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
