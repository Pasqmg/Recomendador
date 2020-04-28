# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rateMovieForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from views.custom_pallet import CustomPalette
from paths import SCORES_PATH


class Ui_RateMovieForm(object):

    def __init__(self, parent=None, db=None, user_id=None, movie_id=None, movie_title=None):
        self.parent = parent
        self.db = db
        self.user_id = user_id
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.scores_path = SCORES_PATH

    def setupUi(self, RateMovieForm):
        RateMovieForm.setObjectName("RateMovieForm")
        RateMovieForm.resize(355, 142)
        self.palette = CustomPalette()
        RateMovieForm.setPalette(self.palette.palette)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RateMovieForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(RateMovieForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.subtitleLabel = QtWidgets.QLabel(RateMovieForm)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.verticalLayout.addWidget(self.subtitleLabel)
        spacerItem = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scoreSlider = QtWidgets.QSlider(RateMovieForm)
        self.scoreSlider.setMaximum(10)
        self.scoreSlider.setProperty("value", 5)
        self.scoreSlider.setOrientation(QtCore.Qt.Horizontal)
        self.scoreSlider.setObjectName("scoreSlider")
        self.horizontalLayout.addWidget(self.scoreSlider)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)

        self.scoreLabel = QtWidgets.QLabel(RateMovieForm)
        self.scoreLabel.setObjectName("scoreLabel")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scoreLabel.setFont(font)
        self.horizontalLayout.addWidget(self.scoreLabel)

        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(RateMovieForm)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RateMovieForm)
        QtCore.QMetaObject.connectSlotsByName(RateMovieForm)

        self.fill_labels()

        self.buttonBox.rejected.connect(lambda: self.cancel_button_clicked(RateMovieForm))
        self.buttonBox.accepted.connect(lambda: self.save_movie_score(RateMovieForm))
        self.scoreSlider.valueChanged.connect(lambda: self.update_label(self.scoreSlider, self.scoreLabel))

    def fill_labels(self):
        self.titleLabel.setText(self.titleLabel.text() + self.movie_title+"?")
        self.scoreLabel.setText(str(self.scoreSlider.value()))

    def update_label(self, slider, label):
        value = slider.value()
        label.setText(str(value))

    def cancel_button_clicked(self, RateMovieForm):
        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setText("The movie was not marked as viewed.")
        msg.setInformativeText("In order to do so, please rate the movie.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setPalette(self.palette.palette)
        res = msg.exec_()
        RateMovieForm.close()

    def save_movie_score(self, RateMovieForm):
        try:
            score = self.scoreSlider.value()
            self.db.save_score(self.user_id, self.movie_id, score)

            msg = QMessageBox()
            msg.setWindowTitle("Rating saved")
            msg.setText("The rating of {} for the movie {} was saved".format(score, self.movie_title))
            msg.setInformativeText("The movie will be added to user's {} history".format(self.user_id))
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setPalette(self.palette.palette)
            res = msg.exec_()
            if res == QMessageBox.Ok:
                self.parent.get_recommendations()
                RateMovieForm.close()

        except FileNotFoundError:
            err = QMessageBox()
            err.setWindowTitle("Error")
            err.setText("Could not save movie rating")
            err.setInformativeText("Movie scores file not found at "+self.scores_path)
            err.setIcon(QMessageBox.Critical)
            err.setStandardButtons(QMessageBox.Ok)
            err.setPalette(self.palette.palette)
            err.exec_()

    def retranslateUi(self, RateMovieForm):
        _translate = QtCore.QCoreApplication.translate
        RateMovieForm.setWindowTitle(_translate("RateMovieForm", "Mark movie as viewed"))
        self.titleLabel.setText(_translate("RateMovieForm", "Did you enjoy "))
        self.subtitleLabel.setText(_translate("RateMovieForm", "Please, rate the movie between 0 and 10."))
        self.scoreLabel.setText(_translate("RateMovieForm", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RateMovieForm = QtWidgets.QWidget()
    ui = Ui_RateMovieForm()
    ui.setupUi(RateMovieForm)
    RateMovieForm.show()
    sys.exit(app.exec_())
