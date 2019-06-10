from GameLogics import Game
from Game_interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem



class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        # мои переменные
        self.g = Game()
        self.g.create_game_matrix()
        self.rect = self.g.getRect()
        self.show_matrix_in_table()

        # Вешаем на кнопки функции
        self.UpButton.clicked.connect(self.up)
        self.DownButton.clicked.connect(self.down)
        self.rightButton.clicked.connect(self.right)
        self.LeftButton.clicked.connect(self.left)
        self.rotateButton.clicked.connect(self.rotate)
        self.startButton.clicked.connect(self.start)

    def keyPressEvent(self, event):
        #print("pressed key " + str(event.key()))
        dict = {
            QtCore.Qt.Key_W: self.up,
            QtCore.Qt.Key_S: self.down,
            QtCore.Qt.Key_A: self.left,
            QtCore.Qt.Key_D: self.right,
            QtCore.Qt.Key_F: self.rotate
        }
        dict[event.key()]()

    def show_matrix_in_table(self):
        for row in range(self.g.GameHeight):
            for col in range(self.g.GameWidth):
                item = self.g[row, col]
                cellinfo = QTableWidgetItem(' ')
                if (row >= self.rect[0][0] and row <= self.rect[0][0] + self.rect[2] - 1) and \
                        (col >= self.rect[0][1] and col <= self.rect[0][1] + self.rect[1] - 1):
                    cellinfo = QTableWidgetItem('selected')
                # Только для чтения
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(row, col, cellinfo)
                arr = [(255, 218, 0), (255, 0, 77)]
                color = arr[item]
                self.tableWidget.item(row, col).setBackground(QtGui.QColor(color[0], color[1], color[2]))


    def decor_update_view(func):
        def wrapped(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.show_matrix_in_table(*args, **kwargs)
        return wrapped

    # Описываем функции
    @decor_update_view
    def rotate(self):
        self.g.rotate_border()


    @decor_update_view
    def up(self):
        self.g.move_border('up')
        self.rect = self.g.getRect()


    @decor_update_view
    def down(self):
        self.g.move_border('down')
        self.rect = self.g.getRect()


    @decor_update_view
    def left(self):
        self.g.move_border('left')
        self.rect = self.g.getRect()


    @decor_update_view
    def right(self):
        self.g.move_border('right')
        self.rect = self.g.getRect()


    def start(self):
        self.g = Game()
        self.g.create_game_matrix()
        self.rect = self.g.getRect()
        self.show_matrix_in_table()
