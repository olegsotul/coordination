import math
import sys

import numpy as np
from PyQt5 import uic, QtWidgets  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MyWidget(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)
        uic.loadUi('solve_exe.ui', self)  # Загружаем дизайн
        self.solve_label.toggled.connect(self.line_r)
        self.SQRT_Solve.toggled.connect(self.sqrt_r)
        self.giper.toggled.connect(self.gip_r)
        self.but_line_solve.clicked.connect(self.solving_line)
        self.but_sqrt_solve.clicked.connect(self.solving_sqrt)
        self.but_gip_solve.clicked.connect(self.solving_gip)

        # координатная ось
        self.plot([0, 0], [-100, 100])
        self.plot([-5, 0], [90, 100])
        self.plot([0, 5], [100, 90])
        self.plot([90, 100], [5, 0])
        self.plot([90, 100], [-5, 0])
        self.plot([90, 100], [5, 0])
        self.plot([80, 88], [-15, -5])
        self.plot([80, 88], [-5, -15])
        self.plot([80, 88], [-15, -5])
        self.plot([-15, -8], [80, 90])
        self.plot([-15, -11], [90, 85])
        self.plot([-100, 100], [0, 0])

    # Выбор графика

    def line_r(self):
        self.linefun.setEnabled(True)
        self.sqrtfun.setEnabled(False)
        self.gipfun.setEnabled(False)

    def sqrt_r(self):
        self.linefun.setEnabled(False)
        self.sqrtfun.setEnabled(True)
        self.gipfun.setEnabled(False)

    def gip_r(self):
        self.linefun.setEnabled(False)
        self.sqrtfun.setEnabled(False)
        self.gipfun.setEnabled(True)

    # Решение линейного графика
    def solving_line(self):
        if self.line_k.text() == '' or self.line_b.text() == '':
            solv = QMessageBox()
            solv.setWindowTitle('Ошибка')
            solv.setText('Не введены значения функции')
            solv.setIcon(QMessageBox.Warning)
            solv.setStandardButtons(QMessageBox.Ok)
            solv.exec_()
        elif float(self.line_k.text()) == 0 and float(self.line_b.text()) == 0:
            solv = QMessageBox()
            solv.setWindowTitle('Ошибка')
            solv.setText('Значения не являются функцией')
            solv.setIcon(QMessageBox.Warning)
            solv.setStandardButtons(QMessageBox.Ok)
            solv.exec_()
        # elif (self.line_k.text().isalpha() == False and self.line_k.text().isnumeric() == False) or \
        #         (self.line_b.text().isalpha() == False and self.line_b.text().isnumeric() == False):
        #     solv = QMessageBox()
        #     solv.setWindowTitle('Ошибка')
        #     solv.setText('Значения не являются функцией')
        #     solv.setIcon(QMessageBox.Warning)
        #     solv.setStandardButtons(QMessageBox.Ok)
        #     solv.exec_()

        else:
            grid = QtWidgets.QGridLayout()
            grid.addWidget(self.graphWidget, 0, 0)
            solv = QMessageBox()
            solv.setWindowTitle('Решение')
            solv.setText(f'Свойства функции y = {self.line_k.text()}x + ({self.line_b.text()})')
            solv.setIcon(QMessageBox.Information)
            solv.setStandardButtons(QMessageBox.Ok)
            if float(self.line_k.text()) > 0:
                up = 'вверх'
            else:
                up = 'вниз'
            solv.setDetailedText(f'Свойства функции: Направлена {up}, Пересечение с Ось y - ({self.line_b.text()})')
            x_coord = []
            y_coord = []
            for i in np.arange(-30.0, 30.0):
                # y = kx + b
                x_coord.append(i)
                y_coord.append(float(self.line_k.text()) * i + float(self.line_b.text()))

            self.plot(x_coord, y_coord)
            solv.exec_()

    # Зарисовка функции
    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)

    # Решение квадратичного графика
    def solving_sqrt(self):
        if self.a_sqrt.text() == '' or self.b_sqrt.text() == '' or self.c_sqrt.text() == '':
            solv = QMessageBox()
            solv.setWindowTitle('Ошибка')
            solv.setText('Не введены значения функции')
            solv.setIcon(QMessageBox.Warning)
            solv.setStandardButtons(QMessageBox.Ok)
            solv.exec_()
        elif float(self.a_sqrt.text()) == 0:
            solv = QMessageBox()
            solv.setWindowTitle('Ошибка')
            solv.setText('Значения не являются квадратичной функцией')
            solv.setIcon(QMessageBox.Warning)
            solv.setStandardButtons(QMessageBox.Ok)
            solv.exec_()
        else:
            grid = QtWidgets.QGridLayout()
            grid.addWidget(self.graphWidget, 0, 0)
            solv = QMessageBox()
            solv.setWindowTitle('Решение')
            solv.setText('Свойства функции\n y = ax^2 +/- bx +/- c')
            discr = int((self.b_sqrt.text())) ** 2 - (4 * int(self.a_sqrt.text()) * int(self.c_sqrt.text()))
            discr_list = []

            if discr > 0:
                x1 = (-int(self.b_sqrt.text()) + math.sqrt(discr)) / (2 * int(self.a_sqrt.text()))
                x2 = (-int(self.b_sqrt.text()) - math.sqrt(discr)) / (2 * int(self.a_sqrt.text()))
                discr_list.append("%.2f" % x1)
                discr_list.append("%.2f" % x2)
            elif discr == 0:
                x = -int(self.b_sqrt.text()) / (2 * int(self.a_sqrt.text()))
                discr_list.append("%.2f" % x)
            else:
                discr_list.append("Корней нет")
            x_h = -int(self.b_sqrt.text()) / (2 * int(self.a_sqrt.text()))
            y_h = float(self.a_sqrt.text()) * (x_h * x_h) + float(self.b_sqrt.text()) * x_h + float(self.c_sqrt.text())
            solv.setIcon(QMessageBox.Information)
            solv.setStandardButtons(QMessageBox.Ok)
            if int(self.a_sqrt.text()) > 0:
                solv.setDetailedText(f'Свойства функции: D = {"%.2f" % discr};\n Корни уравнения = {discr_list};\n '
                                     f'x Вершины = {"%.2f" % x_h};\n y Вершины = {"%.2f" % y_h};\n '
                                     f'Пересечнение с осью y = {float(self.c_sqrt.text())};\n'
                                     f'Возрастает с ({"%.2f" % x_h};+∞);\n'
                                     f'Убывает с (-∞;{"%.2f" % x_h})\n')
            else:
                solv.setDetailedText(f'Свойства функции: D = {"%.2f" % discr};\n Корни уравнения = {discr_list};\n '
                                     f'x Вершины = {"%.2f" % x_h};\n y Вершины = {"%.2f" % y_h};\n '
                                     f'Пересечнение с осью y = {float(self.c_sqrt.text())};\n'
                                     f'Убывает с ({"%.2f" % x_h};+∞);\n'
                                     f'Возрастает с (-∞;{"%.2f" % x_h})\n')
            x_coord = []
            y_coord = []
            for i in range(-15, 15):
                # y = ax^2 +/- bx +/- c
                x_coord.append(i)
                y_coord.append(
                    float(self.a_sqrt.text()) * (i * i) + float(self.b_sqrt.text()) * i + float(self.c_sqrt.text()))

            self.plot(x_coord, y_coord)
            solv.exec_()

    # Решение гиперболы
    def solving_gip(self):
        if self.k_gip.text() == '':
            solv = QMessageBox()
            solv.setWindowTitle('Ошибка')
            solv.setText('Не введены значения функции')
            solv.setIcon(QMessageBox.Warning)
            solv.setStandardButtons(QMessageBox.Ok)
            solv.exec_()
        elif float(self.k_gip.text()) == 0:
            solv = QMessageBox()
            solv.setWindowTitle('Ошибка')
            solv.setText('Значения не являются функцией')
            solv.setIcon(QMessageBox.Warning)
            solv.setStandardButtons(QMessageBox.Ok)
            solv.exec_()
        else:
            grid = QtWidgets.QGridLayout()
            grid.addWidget(self.graphWidget, 0, 0)
            solv = QMessageBox()
            solv.setWindowTitle('Решение')
            solv.setText('Свойства функции ')
            solv.setIcon(QMessageBox.Information)
            solv.setStandardButtons(QMessageBox.Ok)
            if int(self.k_gip.text()) > 0:
                solv.setDetailedText(f'Находиться в I и в III, части координатной плоскости;\n'
                                     f'Невозрастает;\n'
                                     f'Убывает с (-∞;0)V(0;+∞)\n')
            else:
                solv.setDetailedText(f'Находиться в II и в IV, части координатной плоскости;\n'
                                     f'Возрастает (-∞;0)V(0;+∞);\n'
                                     f'Неубывает\n')
            x_coord = []
            y_coord = []

            for i in np.arange(0.1, 20.0, 0.3):
                # y = k/x
                x_coord.append(i)
                y_coord.append(float(self.k_gip.text()) / i)
            self.plot(x_coord, y_coord)
            x_coord = []
            y_coord = []
            for i in np.arange(-20.0, 0.1, 0.3):
                # y = k/x
                x_coord.append(i)
                y_coord.append(float(self.k_gip.text()) / i)
            self.plot(x_coord, y_coord)
            solv.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
