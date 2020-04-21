from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from datamanager.DataLoader import DataLoader


class Ui_NewUserDialog(object):

    def __init__(self, data=None):
        self.username = None
        self.age = None
        self.gender = None
        self.occupation = None

        if data is not None:
            self.username = data["username"]
            self.age = data["age"]
            self.occupation = data["occupation"]
            self.gender = data["gender"]

    def reload_window(self, data):
        #NewUserDialog = QtWidgets.QDialog(self)
        #ui = Ui_NewUserDialog(data)
        #ui.setupUi(NewUserDialog)
        #x = NewUserDialog.exec_()
        self.window = QtWidgets.QDialog()
        self.ui = Ui_NewUserDialog(data)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, NewUserDialog):
        NewUserDialog.setObjectName("NewUserDialog")
        NewUserDialog.resize(460, 320)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 185, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 240, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 212, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 92, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 123, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 220, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 185, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 240, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 212, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 92, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 123, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 220, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 92, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 185, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 240, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 212, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 92, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 123, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 92, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 92, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 185, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        NewUserDialog.setPalette(palette)
        self.widget = QtWidgets.QWidget(NewUserDialog)
        self.widget.setGeometry(QtCore.QRect(50, 50, 351, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.usernameLabel = QtWidgets.QLabel(self.widget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 0, 1, 1)
        self.ageLineEdit = QtWidgets.QLineEdit(self.widget)
        self.ageLineEdit.setObjectName("ageLineEdit")
        self.gridLayout.addWidget(self.ageLineEdit, 7, 1, 1, 1)
        self.occupationComboBox = QtWidgets.QComboBox(self.widget)
        self.occupationComboBox.setObjectName("occupationComboBox")
        self.gridLayout.addWidget(self.occupationComboBox, 9, 1, 1, 1)
        self.occupationLabel = QtWidgets.QLabel(self.widget)
        self.occupationLabel.setObjectName("occupationLabel")
        self.gridLayout.addWidget(self.occupationLabel, 9, 0, 1, 1)
        self.ageLabel = QtWidgets.QLabel(self.widget)
        self.ageLabel.setObjectName("ageLabel")
        self.gridLayout.addWidget(self.ageLabel, 7, 0, 1, 1)
        self.genderLabel = QtWidgets.QLabel(self.widget)
        self.genderLabel.setObjectName("genderLabel")
        self.gridLayout.addWidget(self.genderLabel, 4, 0, 1, 1)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.gridLayout.addWidget(self.usernameLineEdit, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maleRadio = QtWidgets.QRadioButton(self.widget)
        self.maleRadio.setObjectName("maleRadio")
        self.horizontalLayout.addWidget(self.maleRadio)
        self.femaleRadio = QtWidgets.QRadioButton(self.widget)
        self.femaleRadio.setObjectName("femaleRadio")
        self.horizontalLayout.addWidget(self.femaleRadio)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewUserDialog)
        self.buttonBox.accepted.connect(NewUserDialog.accept)
        self.buttonBox.rejected.connect(NewUserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialog)

        self.buttonBox.accepted.connect(self.popup_button)
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


    def popup_button(self):
        username = self.usernameLineEdit.text()
        age_in_text = self.ageLineEdit.text()
        gender = ""
        if self.maleRadio.isChecked():
            gender = "M"
        elif self.femaleRadio.isChecked():
            gender = "F"
        occupation = self.occupationComboBox.currentText()
        try:
            age = int(self.ageLineEdit.text())
            if age < 0 or age > 120:
                raise ValueError
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Format error creating new user")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            info = "The AGE value must be a valid integer between 0 and 120"
            msg.setInformativeText(info)

            # msg.buttonClicked.connect(self.popup_button)
            result = msg.exec_()

            if result:
                data = {}
                data["username"] = username
                data["age"] = age_in_text
                data["gender"] = gender
                data["occupation"] = occupation
                self.reload_window(data)
        return data

    def retranslateUi(self, NewUserDialog):
        _translate = QtCore.QCoreApplication.translate
        NewUserDialog.setWindowTitle(_translate("NewUserDialog", "Register a new user"))
        self.usernameLabel.setText(_translate("NewUserDialog", "Username"))
        self.occupationLabel.setText(_translate("NewUserDialog", "Occupation"))
        self.ageLabel.setText(_translate("NewUserDialog", "Age"))
        self.genderLabel.setText(_translate("NewUserDialog", "Gender"))
        self.maleRadio.setText(_translate("NewUserDialog", "Male"))
        self.femaleRadio.setText(_translate("NewUserDialog", "Female"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewUserDialog = QtWidgets.QDialog()
    ui = Ui_NewUserDialog()
    ui.setupUi(NewUserDialog)
    NewUserDialog.show()
    sys.exit(app.exec_())
