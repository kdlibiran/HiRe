#Imports
import sys
from PySide6.QtWidgets import QApplication
from windows.loginWindow import LoginWindow

# Create the application object
app = QApplication(sys.argv)

window = LoginWindow()
#Start the application
window.show()
app.exec()
