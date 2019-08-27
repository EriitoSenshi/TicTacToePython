from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)


class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setGeometry(200, 200, 600, 600)
        self.startbutton = QPushButton(self)
        self.startbutton.setText("Start!")
        self.startbutton.setGeometry(200, 200, 200, 200)
        self.startbutton.clicked.connect(lambda: startgame())
        self.setWindowTitle("TicTacToe")


def startgame():
    win = Window()
    win.show()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.buttons = []
        self.buttonfont = QFont()
        self.buttonfont.setPointSize(20)
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle("TicTacToe")
        self.xo = True
        self.counter = 0
        self.isgamefinished = False

        for k in range(9):
            self.buttons.append(QPushButton(self))

        self.buttons[0].clicked.connect(lambda: self.buttonclick(0))
        self.buttons[1].clicked.connect(lambda: self.buttonclick(1))
        self.buttons[2].clicked.connect(lambda: self.buttonclick(2))
        self.buttons[3].clicked.connect(lambda: self.buttonclick(3))
        self.buttons[4].clicked.connect(lambda: self.buttonclick(4))
        self.buttons[5].clicked.connect(lambda: self.buttonclick(5))
        self.buttons[6].clicked.connect(lambda: self.buttonclick(6))
        self.buttons[7].clicked.connect(lambda: self.buttonclick(7))
        self.buttons[8].clicked.connect(lambda: self.buttonclick(8))

        for j in range(3):
            for i in range(3):
                if j == 0:
                    self.buttons[i + j].setGeometry(i * 200, j * 200, 200, 200)
                elif j == 1:
                    self.buttons[i + j + 2].setGeometry(i * 200, j * 200, 200, 200)
                else:
                    self.buttons[i + j + 4].setGeometry(i * 200, j * 200, 200, 200)

    def buttonclick(self, n):
        self.counter += 1
        if self.xo:
            self.buttons[n].setText("X")
            self.buttons[n].setFont(self.buttonfont)
            self.xo = False
        else:
            self.buttons[n].setText("O")
            self.buttons[n].setFont(self.buttonfont)
            self.xo = True

        self.buttons[n].setEnabled(False)

        for i in range(0, 9, 3):
            if self.buttons[i].text() == self.buttons[i + 1].text() == self.buttons[i + 2].text():
                if self.buttons[i].text() != "":
                    self.wingame()
        for i in range(3):
            if self.buttons[i].text() == self.buttons[i + 3].text() == self.buttons[i + 6].text():
                if self.buttons[i].text() != "":
                    self.wingame()

        if self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text():
            if self.buttons[0].text() != "":
                self.wingame()
        if self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text():
            if self.buttons[2].text() != "":
                self.wingame()

        if self.counter == 9 and not self.isgamefinished:
            self.drawgame()

    def wingame(self):
        self.isgamefinished = True
        for i in range(9):
            self.buttons[i].setEnabled(False)
        if self.xo:
            print("O wins!")
        else:
            print("X wins!")

    def drawgame(self):
        for i in range(9):
            self.buttons[i].setEnabled(False)
        print("Draw!")


def main():
    mainmenu = MainMenu()
    mainmenu.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
