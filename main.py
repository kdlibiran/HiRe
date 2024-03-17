#Imports
import sys
from PySide6.QtWidgets import QApplication, QWidget

# Create the application object
app = QApplication(sys.argv)

# Create a simple widget
window = QWidget()
window.show()

app.exec()
