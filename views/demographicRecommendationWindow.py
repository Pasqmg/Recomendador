# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demographicRecommendationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView

from DemographicRecommender import DemographicRecommender
from datamanager.DataLoader import DataLoader
from datamanager.ImageGetter import ImageGetter
from views.custom_pallet import CustomPalette


class Ui_DemoRecomWindow(object):

    def __init__(self):
        self.db = DataLoader()
        self.data = None
        self.movies_to_show = None
        self.model = None


    def setupUi(self, DemoRecomWindow):
        DemoRecomWindow.setObjectName("DemoRecomWindow")
        DemoRecomWindow.resize(800, 600)
        self.palette = CustomPalette()
        DemoRecomWindow.setPalette(self.palette.palette)
        self.centralwidget = QtWidgets.QWidget(DemoRecomWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.movieListView = QtWidgets.QListView(self.centralwidget)
        #self.movieListView = QtWidgets.QListWidget(self.centralwidget)
        self.movieListView.setAlternatingRowColors(True)
        self.movieListView.setObjectName("movieListView")
        self.verticalLayout_2.addWidget(self.movieListView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout.addWidget(self.prevButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.user_idSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.user_idSpinBox.setValue(30)
        self.user_idSpinBox.setMinimum(1)
        self.user_idSpinBox.setMaximum(999)
        self.user_idSpinBox.setObjectName("user_idSpinBox")
        self.horizontalLayout_2.addWidget(self.user_idSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.userAmountLabel = QtWidgets.QLabel(self.centralwidget)
        self.userAmountLabel.setObjectName("userAmountLabel")
        self.horizontalLayout_2.addWidget(self.userAmountLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.userInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.userInfoButton.setObjectName("userInfoButton")
        self.horizontalLayout_3.addWidget(self.userInfoButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.getRecommendationButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.getRecommendationButton.sizePolicy().hasHeightForWidth())
        self.getRecommendationButton.setSizePolicy(sizePolicy)
        self.getRecommendationButton.setObjectName("getRecommendationButton")
        self.horizontalLayout_4.addWidget(self.getRecommendationButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(200, 300))
        self.imageLabel.setMaximumSize(QtCore.QSize(200, 300))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_6.addWidget(self.imageLabel)
        self.detailTableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailTableView.sizePolicy().hasHeightForWidth())
        self.detailTableView.setSizePolicy(sizePolicy)
        self.detailTableView.setObjectName("detailTableView")
        self.horizontalLayout_6.addWidget(self.detailTableView)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.viewedButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewedButton.setObjectName("viewedButton")
        self.horizontalLayout_5.addWidget(self.viewedButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        DemoRecomWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DemoRecomWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        DemoRecomWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DemoRecomWindow)
        self.statusbar.setObjectName("statusbar")
        DemoRecomWindow.setStatusBar(self.statusbar)
        # self.centralwidget = QtWidgets.QWidget(DemoRecomWindow)
        # self.centralwidget.setObjectName("centralwidget")
        # self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        # self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        # self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setObjectName("label")
        # self.verticalLayout_2.addWidget(self.label)
        # self.movieListView = QtWidgets.QListView(self.centralwidget)
        # self.movieListView.setObjectName("movieListView")
        # self.verticalLayout_2.addWidget(self.movieListView)
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        # self.prevButton.setObjectName("prevButton")
        # self.horizontalLayout.addWidget(self.prevButton)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout.addItem(spacerItem)
        # self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        # self.nextButton.setObjectName("nextButton")
        # self.horizontalLayout.addWidget(self.nextButton)
        # self.verticalLayout_2.addLayout(self.horizontalLayout)
        # self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        # self.verticalLayout = QtWidgets.QVBoxLayout()
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem1)
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setObjectName("label_2")
        # self.horizontalLayout_2.addWidget(self.label_2)
        # spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem2)
        # self.user_idSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        # self.user_idSpinBox.setValue(30)
        # self.user_idSpinBox.setMinimum(1)
        # self.user_idSpinBox.setMaximum(999)
        # self.user_idSpinBox.setObjectName("user_idSpinBox")
        # self.horizontalLayout_2.addWidget(self.user_idSpinBox)
        # spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem3)
        # self.userAmountLabel = QtWidgets.QLabel(self.centralwidget)
        # self.userAmountLabel.setObjectName("userAmountLabel")
        # self.horizontalLayout_2.addWidget(self.userAmountLabel)
        # self.verticalLayout.addLayout(self.horizontalLayout_2)
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem4)
        # self.userInfoButton = QtWidgets.QPushButton(self.centralwidget)
        # self.userInfoButton.setObjectName("userInfoButton")
        # self.horizontalLayout_3.addWidget(self.userInfoButton)
        # self.verticalLayout.addLayout(self.horizontalLayout_3)
        # spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # self.verticalLayout.addItem(spacerItem5)
        # self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_4.addItem(spacerItem6)
        # self.getRecommendationButton = QtWidgets.QPushButton(self.centralwidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(100)
        # sizePolicy.setHeightForWidth(self.getRecommendationButton.sizePolicy().hasHeightForWidth())
        # self.getRecommendationButton.setSizePolicy(sizePolicy)
        # self.getRecommendationButton.setObjectName("getRecommendationButton")
        # self.horizontalLayout_4.addWidget(self.getRecommendationButton)
        # self.verticalLayout.addLayout(self.horizontalLayout_4)
        # spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout.addItem(spacerItem7)
        # self.detailTableView = QtWidgets.QTableView(self.centralwidget)
        # self.detailTableView.setObjectName("detailTableView")
        # self.verticalLayout.addWidget(self.detailTableView)
        # self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_5.addItem(spacerItem8)
        # self.viewedButton = QtWidgets.QPushButton(self.centralwidget)
        # self.viewedButton.setObjectName("viewedButton")
        # self.horizontalLayout_5.addWidget(self.viewedButton)
        # self.verticalLayout.addLayout(self.horizontalLayout_5)
        # spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout.addItem(spacerItem9)
        # self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        # self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        # self.buttonBox.setObjectName("buttonBox")
        # self.verticalLayout.addWidget(self.buttonBox)
        # self.horizontalLayout_6.addLayout(self.verticalLayout)
        # DemoRecomWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(DemoRecomWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        # self.menubar.setObjectName("menubar")
        # DemoRecomWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(DemoRecomWindow)
        # self.statusbar.setObjectName("statusbar")
        # DemoRecomWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DemoRecomWindow)
        QtCore.QMetaObject.connectSlotsByName(DemoRecomWindow)

        self.init_ui()

    def init_ui(self):
        max_user_id = len(self.db.users_dic)
        self.userAmountLabel.setText("[1 - "+str(max_user_id)+"]")

        self.prevButton.setDisabled(True)
        self.nextButton.setDisabled(True)
        self.detailTableView.setDisabled(True)
        self.viewedButton.setDisabled(True)

        # buttons
        self.userInfoButton.clicked.connect(self.show_user_info)
        self.getRecommendationButton.clicked.connect(self.get_recommendations)
        self.nextButton.clicked.connect(self.show_next_10_items)
        self.prevButton.clicked.connect(self.show_prev_10_items)

        self.movieListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.movieListView.setDragEnabled(False)
        self.movieListView.clicked.connect(self.movielist_clicked)


    def show_user_info(self):
        user_id = int(self.user_idSpinBox.text())
        user = self.db.get_user(user_id)
        msg = QMessageBox()
        msg.setWindowTitle("User info")
        msg.setText("Confirm user")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        info = "ID:\t" + str(user_id) + "\nAge:\t" + str(user.age) + "\nGender:\t" + str(
            user.gender) + "\nOccupation:    " + str(user.occupation)
        msg.setText(info)
        # msg.setInformativeText(info)
        msg.setDetailedText(self.db.print_user_preferences(user_id))
        msg.setPalette(self.palette.palette)
        # msg.buttonClicked.connect(self.popup_button)
        result = msg.exec_()

    def get_recommendations(self):
        # enable next 10 button
        self.nextButton.setDisabled(False)


        user_id = int(self.user_idSpinBox.text())
        self.demo = DemographicRecommender(user_id, self.db)
        movies = self.demo.recommended_items

        # data structure to store all movies
        self.data = []

        for movie in movies:
            # build movie model and add it to the list
            info = movie.print()
            self.data.append(info)
        self.last_movie_index = 10
        #self.movies_to_show = self.data[0:10]
        #self.model = QtCore.QStringListModel(self.movies_to_show)
        self.movieListView.setAlternatingRowColors(True)
        self.show_movies()

    def show_movies(self):
        self.movies_to_show = self.data[self.last_movie_index-10:self.last_movie_index]
        self.model = self.model = QtCore.QStringListModel(self.movies_to_show)
        self.movieListView.setModel(self.model)

    def show_next_10_items(self):
        self.last_movie_index += 10
        if self.last_movie_index > 10:
            self.prevButton.setDisabled(False)
        if self.last_movie_index >= len(self.data):
            self.last_movie_index = len(self.data)
        self.show_movies()

    def show_prev_10_items(self):
        string = str(self.last_movie_index)
        if not string.endswith("0"):
            string = string[0:len(string)-1]
            string += 0
            self.last_movie_index = int(string)
        else:
            self.last_movie_index -= 10
            if self.last_movie_index <= 10:
                self.prevButton.setDisabled(True)
        self.show_movies()

    def movielist_clicked(self):
        #item_id = self.movieListView.currentRow()
        #print("current item",item_id)
        self.set_movie_poster()

    def set_movie_poster(self, message=None):
        if message is None:
            self.imageLabel.setText("UNABLE TO LOAD IMAGE")
        else:
            self.imageLabel.setText(message)
        item = self.movieListView.currentIndex()
        text = item.text()
        item_id = 1
        image_getter = ImageGetter(item_id)
        image = image_getter.img
        #self.imageLabel.setPixmap(QtGui.QPixmap(image))

        self.imageLabel.setPixmap(QtGui.QPixmap("/home/pasqual/PycharmProjects/Recomendador/files/img.jpg"))
        #self.photo.setPixmap(QtGui.QPixmap("dog.jpg"))

    def retranslateUi(self, DemoRecomWindow):
        _translate = QtCore.QCoreApplication.translate
        DemoRecomWindow.setWindowTitle(_translate("DemoRecomWindow", "Demographic Recommendation"))
        self.label.setText(_translate("DemoRecomWindow", "Demographic Recommendation"))
        self.prevButton.setText(_translate("DemoRecomWindow", "Prev. 10"))
        self.nextButton.setText(_translate("DemoRecomWindow", "Next 10"))
        self.label_2.setText(_translate("DemoRecomWindow", "User"))
        self.userAmountLabel.setText(_translate("DemoRecomWindow", "1 to 943"))
        self.userInfoButton.setText(_translate("DemoRecomWindow", "User info"))
        self.getRecommendationButton.setText(_translate("DemoRecomWindow", "Get recommendation"))
        self.viewedButton.setText(_translate("DemoRecomWindow", "Mark as viewed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DemoRecomWindow = QtWidgets.QMainWindow()
    ui = Ui_DemoRecomWindow()
    ui.setupUi(DemoRecomWindow)
    DemoRecomWindow.show()
    sys.exit(app.exec_())
