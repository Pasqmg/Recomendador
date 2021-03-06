# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from datamanager.DataLoader import DataLoader
from views.userPreferencesWidget import Ui_NewUserPreferencesWidget
from views.light_custom_pallet import LightCustomPalette

class Ui_NewUserWindow(object):

    def __init__(self, db, data=None):
        self.db = db
        self.username = None
        self.age = None
        self.gender = None
        self.occupation = None

        if data is not None:
            self.username = data["username"]
            self.age = data["age"]
            self.occupation = data["occupation"]
            self.gender = data["gender"]

    def setupUi(self, NewUserWindow):
        NewUserWindow.setObjectName("MainWindow")
        NewUserWindow.resize(460, 320)
        self.palette = LightCustomPalette()
        NewUserWindow.setPalette(self.palette.palette)
        self.centralwidget = QtWidgets.QWidget(NewUserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 351, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.usernameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 0, 1, 1)
        self.ageLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ageLineEdit.setObjectName("ageLineEdit")
        self.gridLayout.addWidget(self.ageLineEdit, 7, 1, 1, 1)
        self.occupationComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.occupationComboBox.setObjectName("occupationComboBox")
        self.gridLayout.addWidget(self.occupationComboBox, 9, 1, 1, 1)
        self.occupationLabel = QtWidgets.QLabel(self.layoutWidget)
        self.occupationLabel.setObjectName("occupationLabel")
        self.gridLayout.addWidget(self.occupationLabel, 9, 0, 1, 1)
        self.ageLabel = QtWidgets.QLabel(self.layoutWidget)
        self.ageLabel.setObjectName("ageLabel")
        self.gridLayout.addWidget(self.ageLabel, 7, 0, 1, 1)
        self.genderLabel = QtWidgets.QLabel(self.layoutWidget)
        self.genderLabel.setObjectName("genderLabel")
        self.gridLayout.addWidget(self.genderLabel, 4, 0, 1, 1)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.gridLayout.addWidget(self.usernameLineEdit, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maleRadio = QtWidgets.QRadioButton(self.layoutWidget)
        self.maleRadio.setObjectName("maleRadio")
        self.horizontalLayout.addWidget(self.maleRadio)
        self.femaleRadio = QtWidgets.QRadioButton(self.layoutWidget)
        self.femaleRadio.setObjectName("femaleRadio")
        self.horizontalLayout.addWidget(self.femaleRadio)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(50, 240, 349, 25))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        NewUserWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewUserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 22))
        self.menubar.setObjectName("menubar")
        NewUserWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewUserWindow)
        self.statusbar.setObjectName("statusbar")
        NewUserWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewUserWindow)
        QtCore.QMetaObject.connectSlotsByName(NewUserWindow)

        self.buttonBox.accepted.connect(lambda: self.ok_button_clicked(NewUserWindow))
        self.buttonBox.rejected.connect(lambda: self.cancel_button_clicked(NewUserWindow))
        self.fill_occupation_comboBox()
        self.fill_values()

    def fill_values(self):
        if self.username is not None:
            self.usernameLineEdit.setText(self.username)
        if self.age is not None:
            self.ageLineEdit.setText(self.age)
        if self.gender is not None:
            if self.gender == "M":
                self.maleRadio.setChecked(True)
            elif self.gender == "F":
                self.femaleRadio.setChecked(True)
        if self.occupation is not None:
            self.default_comboBox(self.occupation)


    def fill_occupation_comboBox(self):
        db = DataLoader()
        occupation_list = db.get_occupation_list()
        self.occupationComboBox.addItems(occupation_list)
        self.default_comboBox()

    def default_comboBox(self, occupation='none'):
        index = self.occupationComboBox.findText(occupation, QtCore.Qt.MatchFixedString)
        self.occupationComboBox.setCurrentIndex(index)

    def ok_button_clicked(self, NewUserWindow):
        error = False
        username = self.usernameLineEdit.text()

        parts = username.split()
        if len(parts) > 1:
            error = True
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Value error creating new user")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            info = "The USERNAME cannot contain whitespaces"
            msg.setInformativeText(info)
            result = msg.exec_()
        elif username in self.db.usernames_list:
            error = True
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The username \"{}\" is not available".format(username))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            info = "Please choose a different username"
            msg.setInformativeText(info)
            result = msg.exec_()

        age_in_text = self.ageLineEdit.text()
        gender = ""
        if self.maleRadio.isChecked():
            gender = "M"
        elif self.femaleRadio.isChecked():
            gender = "F"
        else:
            error = True
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Value error creating new user")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            info = "The GENDER value must be specified"
            msg.setInformativeText(info)
            result = msg.exec_()
        occupation = self.occupationComboBox.currentText()
        try:
            age = int(self.ageLineEdit.text())
            if age < 0 or age > 120:
                raise ValueError
        except ValueError:
            error = True
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Format error creating new user")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            info = "The AGE value must be a valid integer between 0 and 120"
            msg.setInformativeText(info)
            result = msg.exec_()

        # if all data is fine, ask the user if it wants to set preferences
        if not error:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("User information")
            msg.setText("Create user with the following information?")
            if username != "":
                info = "Username:\t"+username+"\nAge:\t"+str(age)+"\nGender:\t"+gender+"\nOccupation:\t"+occupation
            else:
                info = "\nAge:\t" + str(age) + "\nGender:\t" + gender + "\nOccupation:\t" + occupation
            msg.setInformativeText(info)
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            res = msg.exec_()

            if res == QMessageBox.Ok:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Question)
                msg.setWindowTitle("Set user preferences?")
                msg.setText("Would you like to define user movie genre preferences?")
                msg.setInformativeText("If not, random preferences will be defined")
                msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
                #msg.setDefaultButton(QMessageBox.No)

                result = msg.exec_()

                if result == QMessageBox.Yes:
                    #show user preferences window
                    self.NewUserPreferencesWidget = QtWidgets.QWidget()
                    self.ui = Ui_NewUserPreferencesWidget(self.db, username, age, gender, occupation)
                    self.ui.setupUi(self.NewUserPreferencesWidget)
                    self.NewUserPreferencesWidget.show()
                    NewUserWindow.close()
                else:
                    self.db.save_user(username, age, gender, occupation)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("User successfully created")
                    msg.setText("New user registered with ID {}".format(len(self.db.users_dic)))
                    msg.setStandardButtons(QMessageBox.Ok)
                    res = msg.exec_()
                    NewUserWindow.close()

    def cancel_button_clicked(self, NewUserWindow):
        NewUserWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register a new user"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.occupationLabel.setText(_translate("MainWindow", "Occupation"))
        self.ageLabel.setText(_translate("MainWindow", "Age"))
        self.genderLabel.setText(_translate("MainWindow", "Gender"))
        self.maleRadio.setText(_translate("MainWindow", "Male"))
        self.femaleRadio.setText(_translate("MainWindow", "Female"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewUserWindow = QtWidgets.QMainWindow()
    ui = Ui_NewUserWindow()
    ui.setupUi(NewUserWindow)
    NewUserWindow.show()
    sys.exit(app.exec_())
