from PyQt5.QtWidgets import *
from ui_py_files import OutputParameterWidget
from models import OutputParameterModel


class OutputParameterController(QWidget, OutputParameterWidget):

    def __init__(self) -> None:
        super().__init__()
        self.init_window()

    def init_window(self):
        self.setupUi(self)
        self._values = OutputParameterModel()
        self.comboBox.currentIndexChanged.connect(self.combo_box_changed)
        self.lineEdit.textChanged.connect(self.name_changed)

    def name_changed(self, text):
        self._values.name = text

    def combo_box_changed(self, index):
        selected_item = self.comboBox.currentText()
        self.values.type = selected_item

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values: OutputParameterModel):
        if not isinstance(values, OutputParameterModel):
            raise ValueError("values must be type of OutputParameterModel")
        self._values = values
