from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from .signUpWindow import SignUpWindow
from components.QLabelClick import QLabelClick
#import pointer cursor
import PySide6.QtCore


class LoginWindow(QWidget):
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
        self.setGeometry(400, 400, 800, 800)

        self.layout = QVBoxLayout()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.layout.addWidget(self.username)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.layout.addWidget(self.password)
        self.loginBtn = QPushButton("Login", self)
        self.loginBtn.clicked.connect(self.login)
        
        # Add connection to sign up window
        self.signUpLabel1 = QLabel("Don't have an account?")
        self.signUpLabel = QLabelClick("Sign Up",self)
        #bold
        self.signUpLabel.setStyleSheet("font: bold")
        #change arrow cursor to hand cursor
        self.signUpLabel.setCursor(PySide6.QtCore.Qt.PointingHandCursor)
        self.signUpLabel.clicked.connect(self.showSignUp)
        
        self.layout.addWidget(self.loginBtn)
        self.layout.addWidget(self.signUpLabel1)
        self.layout.addWidget(self.signUpLabel)

        self.setLayout(self.layout)
        self.show()
