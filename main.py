#Imports
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from windows.loginWindow import LoginWindow

# Create the application object
app = QApplication(sys.argv)

window = QMainWindow()
loginWindow = LoginWindow()
window.setCentralWidget(loginWindow)

#Start the application
window.show()
app.exec()
