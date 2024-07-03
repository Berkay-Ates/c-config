from PyQt5.QtWidgets import QApplication
from controllers import MainWindowController

app = QApplication([])
window = MainWindowController()
window.show()
app.exec_()
