from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

f=open("post.txt", "a+")

class post:

    def yangi_post(self):
        y_post=input("postni yozing: ")
        f.write(y_post)
        print("yangi post yaratildi")

    def post_oqish(self):
        print("Sizni postlaringiz: ")
        hamma=f.read()
        print(hamma)

f.close()
