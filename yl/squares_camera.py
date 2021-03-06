import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.show_btn.setObjectName("show_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 10, 91, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 0, 131, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_side = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_side.setObjectName("lineEdit_side")
        self.verticalLayout_2.addWidget(self.lineEdit_side)
        self.lineEdit_k = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_k.setObjectName("lineEdit_k")
        self.verticalLayout_2.addWidget(self.lineEdit_k)
        self.lineEdit_n = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.verticalLayout_2.addWidget(self.lineEdit_n)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 371, 241))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????-???????????????? ??? 1"))
        self.show_btn.setText(_translate("MainWindow", "????????????????"))
        self.label_2.setText(_translate("MainWindow", "side"))
        self.label_3.setText(_translate("MainWindow", "coeff"))
        self.label.setText(_translate("MainWindow", "n"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('camera_image.ui', self)
        self.setupUi(self)
        self.do_paint = False
        self.show_btn.clicked.connect(self.paint)

    # ?????????? ??????????????????????, ?????????? ?????????????? ????????
    # ???????????????????????? ???????? ????????????????????,
    # ????????????????, ?????? ???????????????? ??????????
    def paintEvent(self, event):
        if self.do_paint is True:
            # ?????????????? ???????????? QPainter ?????? ??????????????????
            qp = QPainter(self)
            # ???????????????? ?????????????? ??????????????????
            qp.begin(self)
            self.draw_flag(qp)
            # ?????????????????? ??????????????????
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        print('Paint')
        side = int(self.lineEdit_side.text())
        k = float(self.lineEdit_k.text())
        n = int(self.lineEdit_n.text())
        # ???????????? ??????????
        qp.setPen(QColor(255, 0, 0))
        # ???????????? ?????????????????????????? ???????????????? ????????????
        x = 30
        y = 180


        qp.drawRect(x, y, int(side), int(side))
        for i in range(1, n):
            qp.drawRect(x + ((side - side * k ** i) // 2), y + ((side - side * k ** i) // 2), side * k ** i,
                        side * k ** i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
