from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton
from PySide6.QtCore import QSize, Qt

import sys

 #Application handler. Si possono passare sys.arg
#window = QMainWindow() #In Qt all top level widgets are windows --. QMainWindows pre-made
# widget which provides a lot of standard window features
# that is, they don't have a parent and are not nested within another widget or layout.
#window.show() #default is windows are hidden
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Driver UI")
        button = QPushButton("Inizia navigazione")
        self.setCentralWidget(button)

app = QApplication([])

window = MainWindow()
window.show()
app.exec()
