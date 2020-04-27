from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView

from CollaborativeRecommender import CollaborativeRecommender
from datamanager.DataLoader import DataLoader
from views.custom_pallet import CustomPalette


class Ui_CollabRecomWindow(object):

    def __init__(self):
        self.db = DataLoader()
        self.data = None
        self.movies_to_show = None
        self.model = None
        self.demo = None
        self.recommended_items = []
        self.active_items = []


    def setupUi(self, CollabRecomWindow):
        CollabRecomWindow.setObjectName("CollabRecomWindow")
        CollabRecomWindow.resize(800, 600)
        self.palette = CustomPalette()
        CollabRecomWindow.setPalette(self.palette.palette)
        self.centralwidget = QtWidgets.QWidget(CollabRecomWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.movieListView = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movieListView.sizePolicy().hasHeightForWidth())
        self.movieListView.setSizePolicy(sizePolicy)
        self.movieListView.setObjectName("movieListView")
        self.verticalLayout_2.addWidget(self.movieListView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout.addWidget(self.prevButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.user_idSpinBox = QtWidgets.QSpinBox(self.frame_2)
        self.user_idSpinBox.setMinimum(1)
        self.user_idSpinBox.setMaximum(999)
        self.user_idSpinBox.setProperty("value", 30)
        self.user_idSpinBox.setObjectName("user_idSpinBox")
        self.horizontalLayout_2.addWidget(self.user_idSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.userAmountLabel = QtWidgets.QLabel(self.frame_2)
        self.userAmountLabel.setObjectName("userAmountLabel")
        self.horizontalLayout_2.addWidget(self.userAmountLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.userInfoButton = QtWidgets.QPushButton(self.frame_2)
        self.userInfoButton.setObjectName("userInfoButton")
        self.horizontalLayout_3.addWidget(self.userInfoButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.frame_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem5)
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
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.imageLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(200, 300))
        self.imageLabel.setMaximumSize(QtCore.QSize(200, 300))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_7.addWidget(self.imageLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.titleLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout_6.addWidget(self.titleLabel)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.yearLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearLabel.sizePolicy().hasHeightForWidth())
        self.yearLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")
        self.horizontalLayout_10.addWidget(self.yearLabel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.stariconLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(24)
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(self.stariconLabel.sizePolicy().hasHeightForWidth())
        self.stariconLabel.setSizePolicy(sizePolicy)
        self.stariconLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.stariconLabel.setText("")
        self.stariconLabel.setPixmap(QtGui.QPixmap("../images/star.png"))
        self.stariconLabel.setScaledContents(True)
        self.stariconLabel.setObjectName("stariconLabel")
        self.horizontalLayout_9.addWidget(self.stariconLabel)
        self.scoreLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scoreLabel.sizePolicy().hasHeightForWidth())
        self.scoreLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setObjectName("scoreLabel")
        self.horizontalLayout_9.addWidget(self.scoreLabel)
        self.label_6 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.genresLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genresLabel.sizePolicy().hasHeightForWidth())
        self.genresLabel.setSizePolicy(sizePolicy)
        self.genresLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.genresLabel.setObjectName("genresLabel")
        self.verticalLayout.addWidget(self.genresLabel)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addWidget(self.frame)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.viewedButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewedButton.setObjectName("viewedButton")
        self.horizontalLayout_5.addWidget(self.viewedButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem11)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        CollabRecomWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CollabRecomWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        CollabRecomWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CollabRecomWindow)
        self.statusbar.setObjectName("statusbar")
        CollabRecomWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CollabRecomWindow)
        QtCore.QMetaObject.connectSlotsByName(CollabRecomWindow)

        self.buttonBox.rejected.connect(lambda:self.cancel_button_clicked(CollabRecomWindow))
        self.buttonBox.accepted.connect(lambda:self.ok_button_clicked(CollabRecomWindow))

        self.init_ui()

    def init_ui(self):
        max_user_id = len(self.db.users_dic)
        self.userAmountLabel.setText("[1 - "+str(max_user_id)+"]")

        self.prevButton.setDisabled(True)
        self.nextButton.setDisabled(True)
        #self.detailListView.setDisabled(True)
        self.viewedButton.setDisabled(True)

        # buttons
        self.userInfoButton.clicked.connect(self.show_user_info)
        self.getRecommendationButton.clicked.connect(self.get_recommendations)
        self.nextButton.clicked.connect(self.show_next_10_items)
        self.prevButton.clicked.connect(self.show_prev_10_items)

        self.movieListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.movieListView.setDragEnabled(False)
        self.movieListView.clicked.connect(self.movielist_clicked)
        #self.movieListView.currentItemChanged.connect(self.movielist_clicked)


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
        self.prevButton.setDisabled(True)

        user_id = int(self.user_idSpinBox.text())
        self.collab = CollaborativeRecommender(user_id, self.db)
        self.recommended_items = self.collab.recommended_items

        # data structure to store all movies
        self.data = []

        for movie in self.recommended_items:
            # build movie model and add it to the list
            info = movie.print()
            self.data.append(info)
        self.last_movie_index = 10
        #self.movies_to_show = self.data[0:10]
        #self.model = QtCore.QStringListModel(self.movies_to_show)
        self.movieListView.setAlternatingRowColors(True)
        self.show_movies()

    def show_movies(self):
        self.movieListView.clear()
        self.movies_to_show = self.data[self.last_movie_index-10:self.last_movie_index]
        # update active items
        self.active_items = self.recommended_items[self.last_movie_index-10:self.last_movie_index]
        for movie in self.movies_to_show:
            self.movieListView.addItem(movie)
        self.movieListView.currentItemChanged.connect(self.movielist_clicked)
        self.movieListView.setCurrentRow(0)
        #slf.model = QtCore.QStringListModel(self.movies_to_show)
        #self.movieListView.setModel(self.emodel)

    def show_next_10_items(self):
        self.movieListView.currentItemChanged.connect(self.do_nothing)
        self.last_movie_index += 10
        if self.last_movie_index > 10:
            self.prevButton.setDisabled(False)
        if self.last_movie_index >= len(self.data):
            self.last_movie_index = len(self.data)
        self.show_movies()

    def show_prev_10_items(self):
        self.movieListView.currentItemChanged.connect(self.do_nothing)
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
        self.show_movie_detail()

    def set_movie_poster(self, message=None):

        item = self.movieListView.currentItem()
        if item is not None:
            title = item.text().split("\n")[0]
            print("Item:",title)
            try:
                path = "/home/pasqual/PycharmProjects/Recomendador/images/"+title+".jpg"
                self.imageLabel.setPixmap(QtGui.QPixmap(path))
            except:
                if message is None:
                    self.imageLabel.setText("UNABLE TO LOAD IMAGE")
                else:
                    self.imageLabel.setText(message)
        else:
            if message is None:
                self.imageLabel.setText("UNABLE TO LOAD IMAGE")
            else:
                self.imageLabel.setText(message)
        #item_id = 1
        #image_getter = ImageGetter(item_id)
        #image = image_getter.img
        #self.imageLabel.setPixmap(QtGui.QPixmap(image))

        #self.imageLabel.setPixmap(QtGui.QPixmap("/home/pasqual/PycharmProjects/Recomendador/files/img.jpg"))
        #self.photo.setPixmap(QtGui.QPixmap("dog.jpg"))

    def show_movie_detail(self):
        #self.detailListView.setDisabled(False)
        index = self.movieListView.currentRow()
        item = self.active_items[index]
        self.titleLabel.setText(str(item.get_title()))
        self.yearLabel.setText(" "+str(item.get_year()))
        self.scoreLabel.setText(str(round(self.db.get_movie_avg_score(item.id)/10,1)))
        self.genresLabel.setText(" Genres:\n"+str(self.db.get_movie_genres(item.id)))
        #self.detailListView.setModel(self.model)
        #self.detailListView.addItem(item.print())
        #print("Current index is ",index)

    def ok_button_clicked(self, CollabRecomWindow):
        CollabRecomWindow.close()

    def cancel_button_clicked(self, CollabRecomWindow):
        CollabRecomWindow.close()


    def retranslateUi(self, CollabRecomWindow):
        _translate = QtCore.QCoreApplication.translate
        CollabRecomWindow.setWindowTitle(_translate("CollabRecomWindow", "Collaborative Recommendation"))
        self.label.setText(_translate("CollabRecomWindow", "Collaborative Recommendation"))
        self.prevButton.setText(_translate("CollabRecomWindow", "Prev. 10"))
        self.nextButton.setText(_translate("CollabRecomWindow", "Next 10"))
        self.label_2.setText(_translate("CollabRecomWindow", "User"))
        self.userAmountLabel.setText(_translate("CollabRecomWindow", "1 to 943"))
        self.userInfoButton.setText(_translate("CollabRecomWindow", "User info"))
        self.getRecommendationButton.setText(_translate("CollabRecomWindow", "Get recommendation"))
        self.imageLabel.setText(_translate("CollabRecomWindow", ""))
        self.titleLabel.setText(_translate("CollabRecomWindow", "Title"))
        self.yearLabel.setText(_translate("CollabRecomWindow", "(year)"))
        self.label_3.setText(_translate("CollabRecomWindow", " User rating"))
        self.scoreLabel.setText(_translate("CollabRecomWindow", "0.0"))
        self.label_6.setText(_translate("CollabRecomWindow", "/10"))
        self.genresLabel.setText(_translate("CollabRecomWindow", " Genres"))
        self.viewedButton.setText(_translate("CollabRecomWindow", "Mark as viewed"))

    def do_nothing(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CollabRecomWindow = QtWidgets.QMainWindow()
    ui = Ui_CollabRecomWindow()
    ui.setupUi(CollabRecomWindow)
    CollabRecomWindow.show()
    sys.exit(app.exec_())