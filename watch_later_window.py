import os
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join('data', 'watch_later.ui'), self)
        self.setWindowTitle("Смотреть позже")
        self.btn_search.clicked.connect(self.search_2)
        self.search_2()
        self.btn_goback.clicked.connect(self.close)

    def search_2(self):
        try:

            con1 = sqlite3.connect('sakilaDB.db')
            cur1 = con1.cursor()
            search_temp = self.search_title.text()
            result2 = cur1.execute(f"""SELECT film_id, title, fav_films.id, poster_name
                                        FROM film 
                                        left join fav_films on fav_films.id_film = film.film_id
                                        WHERE title LIKE '%{search_temp}%' AND fav_films.id is not Null""").fetchall()
            film = []

            for elem in result2:
                film.append(elem)
            count = 0
            for i in range(3):
                for j in range(6):
                    if count < len(film):
                        self.test_widget = Ui_Form_2(film[count])
                        self.test_widget.setupUi_2()
                        self.grid.addWidget(self.test_widget, i, j)
                    else:
                        pass
                    count += 1
            print(film)

        except Exception as ex:
            print('ERROR!! - ' + str(ex))


class Ui_Form_2(QWidget):
    def __init__(self, film):
        super().__init__()
        self.id = film[0]
        self.title = film[1]
        self.temp = film[2]
        self.poster = film[3]
        self._translate = None

    def setupUi_2(self):
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
        if self.poster != None:
            fullname = os.path.join('data', self.poster)
            try:
                self.film_poster_2.setPixmap(QtGui.QPixmap(fullname))
            except Exception as ex:
                print('ERROR!! - ' + str(ex))

        else:
            fullname = os.path.join('data', 'no_poster.png')
            self.film_poster_2.setPixmap(QtGui.QPixmap(fullname))
        self.film_poster_2.setScaledContents(True)
        self.film_poster_2.setObjectName("film_poster_2")
        self.film_bg_2 = QtWidgets.QLabel(self.groupBox)
        self.film_bg_2.setGeometry(QtCore.QRect(0, 190, 161, 101))
        self.film_bg_2.setText("")
        fullname = os.path.join('data', "backgroung.png")
        self.film_bg_2.setPixmap(QtGui.QPixmap(fullname))
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
        self.btn_watch_later_2.clicked.connect(self.add_fav_film)

        self.retranslateUi_2(self)
        self.film_name_2.setText(
            f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:400;\">{self.title}</span></p></body></html>")
        self.btn_watch_later_2.setText("- Смотреть Позже")

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_2(self, Form):
        pass
        # self._translate = QtCore.QCoreApplication.translate

    def add_fav_film(self):
        try:
            con = sqlite3.connect('sakilaDB.db')
            cur = con.cursor()
            cur.execute("""DELETE FROM fav_films WHERE id = ? """, (self.temp,))
            con.commit()
            con.close()
            self.deleteLater()
        except Exception as ex:
            print('ERROR!! - ' + str(ex))