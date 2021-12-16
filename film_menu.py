# from main import count as count_from_main
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_Form(QWidget):
    # count = count_from_main
    con = sqlite3.connect('sakilaDB.db')
    cur = con.cursor()

    result1 = cur.execute("""SELECT film_id FROM film;""").fetchall()
                             # WHERE film_id=(SELECT MAX(film_id) from film);""").fetchall()

    for elem in result1:
        pass
    def setupUi(self):
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 161, 291))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.film_poster_2 = QtWidgets.QLabel(self.groupBox)
        self.film_poster_2.setGeometry(QtCore.QRect(0, 0, 161, 191))
        self.film_poster_2.setMinimumSize(QtCore.QSize(161, 0))
        self.film_poster_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.film_poster_2.setText("")
        self.film_poster_2.setPixmap(QtGui.QPixmap("duna.jpg"))
        self.film_poster_2.setScaledContents(True)
        self.film_poster_2.setObjectName("film_poster_2")
        self.film_bg_2 = QtWidgets.QLabel(self.groupBox)
        self.film_bg_2.setGeometry(QtCore.QRect(0, 190, 161, 101))
        self.film_bg_2.setText("")
        self.film_bg_2.setPixmap(QtGui.QPixmap("backgroung.png"))
        self.film_bg_2.setScaledContents(True)
        self.film_bg_2.setObjectName("film_bg_2")
        self.film_name_2 = QtWidgets.QLabel(self.groupBox)
        self.film_name_2.setGeometry(QtCore.QRect(20, 190, 121, 31))
        self.film_name_2.setObjectName("film_name_2")
        self.btn_watch_later_2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_watch_later_2.setGeometry(QtCore.QRect(20, 240, 121, 23))
        self.btn_watch_later_2.setAutoDefault(False)
        self.btn_watch_later_2.setDefault(False)
        self.btn_watch_later_2.setFlat(False)
        self.btn_watch_later_2.setObjectName("btn_watch_later_2")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.film_name_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Империум</span></p></body></html>"))
        self.btn_watch_later_2.setText(_translate("Form", "+ Смотреть Позже"))



