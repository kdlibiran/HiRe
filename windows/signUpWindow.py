from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QWidget
from .loginWindow import LoginWindow

class SignUpWindow(QWidget):
    def signUp(self):
        print(self.username.text())
        print(self.password.text())

    def showLogin(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        self.hide()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HiRe - SignUp")
        self.setGeometry(400, 200, 800, 400)

        self.username = QLineEdit(self)
        self.username.move(150, 50)
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit(self)
        self.password.move(150, 100)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.signUpBtn = QPushButton("Sign Up", self)
        self.signUpBtn.move(150, 150)
        self.signUpBtn.clicked.connect(self.signUp)

        # Add connection to login window
        self.loginBtn = QPushButton("Login", self)
        self.loginBtn.move(150, 200)
        self.loginBtn.clicked.connect(self.showLogin)
