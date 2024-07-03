from PyQt5.QtWidgets import *
from ui_py_files import InputParameterWidget
from models import InputParameterModel


class InputParameterController(QWidget, InputParameterWidget):

    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.setupUi(self)
        self.values = InputParameterModel()
