import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        global count
        count = 1
        self.btn_search.clicked.connect(self.search)

    def search(self):
        global count, film
        try:
            text = str(self.search_filter.currentText())
            if text == 'Название':
                con1 = sqlite3.connect('sakilaDB.db')
                cur1 = con1.cursor()
                search_temp = self.search_title.text()
                result2 = cur1.execute(f"""SELECT film_id, title FROM film
                    WHERE title LIKE '%{search_temp}%'""").fetchall()
                film = {}

                for elem in result2:
                    film[elem[0]] = elem[1]
                for i in range(3):
                    for j in range(6):
                        self.test_widget = Ui_Form()
                        self.test_widget.setupUi()
                        self.grid.addWidget(self.test_widget, i, j)
                        count += 1
                print(film)

        except Exception as ex:
            print('ERROR!! - ' + str(ex))


class Ui_Form(QWidget):
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
        self.btn_watch_later_2.clicked.connect(self.add_fav_film)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        film_name = film[count]
        _translate = QtCore.QCoreApplication.translate
        self.film_name_2.setText(_translate("Form",
                                            f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:400;\">{film_name}</span></p></body></html>"))
        self.btn_watch_later_2.setText(_translate("Form", "+ Смотреть Позже"))

    def add_fav_film(self):
        con = sqlite3.connect('sakilaDB.db')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM fav_films""").fetchall()
        param = {}

        for elem in result:
            param[elem[0]] = elem[1]
        con.close()
        max_key = max(param.keys()) + 1
        con = sqlite3.connect('sakilaDB.db')
        cur = con.cursor()
        result = cur.execute("""INSERT INTO fav_films(id,id_film) VALUES() """).fetchall()
        param = {}

        for elem in result:
            param[elem[0]] = elem[0]
        print(param)
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
