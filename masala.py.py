from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

f=open("parol_va_nicklar.txt","a+")
fs=f.read()
class u_kirish:
    
    def login():
        input("Nickname: ")
        input("Parol: ")

        print("Akkauntingizga kirdingiz ")

    def new_acc():

        f.write(input("Yangi nickname yozing: "))
        f.write(input("Yangi parol yarating: "))
f.close
