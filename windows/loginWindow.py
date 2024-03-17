from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit
from .signUpWindow import SignUpWindow

class LoginWindow(QMainWindow):
    def login(self):
        print(self.username.text())
        print(self.password.text())

    def showSignUp(self):
        self.signUpWindow = SignUpWindow()
        self.signUpWindow.show()
        self.hide()


    def __init__(self):
        super().__init__()

        self.setWindowTitle("HiRe - Login")
        self.setGeometry(200, 200, 800, 400)

        self.username = QLineEdit(self)
        self.username.move(150, 50)
        self.username.setPlaceholderText("Username")
        
        self.password = QLineEdit(self)
        self.password.move(150, 100)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.loginBtn = QPushButton("Login", self)
        self.loginBtn.move(150, 150)
        self.loginBtn.clicked.connect(self.login)

        # Add connection to sign up window
        self.signUpBtn = QPushButton("Sign Up", self)
        self.signUpBtn.move(150, 200)
        self.signUpBtn.clicked.connect(self.showSignUp)
        

        

