import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

# con = sqlite3.connect('sakilaDB.db')
# cur = con.cursor()
#
# result1 = cur.execute("""SELECT * FROM film;""").fetchall()
# # WHERE film_id=(SELECT MAX(film_id) from film);""").fetchall()
# film = {}
#
# for elem in result1:
#     film[elem[0]] = elem[1]


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
                # NameP = itemsoft['name']
                # s = 'SELECT * FROM program WHERE (name LIKE "' + NameP + '%%")'
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
            # elif text == 'Жанр':
            #     con1 = sqlite3.connect('sakilaDB.db')
            #     cur1 = con1.cursor()
            #
            #     result2 = cur1.execute("""SELECT title FROM film
            #         WHERE title LIKE '%Жанр%';""").fetchall()
            #     film = {}
            #
            #     for elem in result2:
            #         film[elem[0]] = elem[1]
            #     count = 0
            #     for i in range(3):
            #         for j in range(6):
            #             self.test_widget = Ui_Form()
            #             self.test_widget.setupUi()
            #             self.grid.addWidget(self.test_widget, i, j)
            #             count += 1

        except Exception as ex:
            print('ERROR!! - ' + str(ex))

    #     for i in reversed(range(self.grid.count())):
    #         self.test_widget = self.grid.itemAt(i).widget()
    #         # чистим layout
    #         self.grid.removeWidget(self.test_widget)
    #         # чистим gui
    #         self.test_widget.setParent(None)


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

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        film_name = film[count]
        _translate = QtCore.QCoreApplication.translate
        self.film_name_2.setText(_translate("Form",
                                            f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:400;\">{film_name}</span></p></body></html>"))
        self.btn_watch_later_2.setText(_translate("Form", "+ Смотреть Позже"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
