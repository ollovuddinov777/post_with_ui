from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from masala import u_kirish
from post import post
class myclass(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(250, 250)

        self.yangi_akk=QPushButton("new", self)
        self.yangi_akk.move(75, 20)
        self.yangi_akk.clicked.connect(u_kirish.new_acc)

        self.login=QPushButton("login", self)
        self.login.move(75, 50)
        self.login.clicked.connect(u_kirish.login)


app=QApplication([])
win=myclass()
win.show()
app.exec_()
