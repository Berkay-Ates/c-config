from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, QObject, pyqtSignal
from ui_py_files import InputParameterWidget
from models import InputParameterModel
from PyQt5.QtCore import Qt
from ui_py_files import InfoPopup


class InputParameterController(QWidget, InputParameterWidget):

    struct_signal = pyqtSignal(QObject)

    def __init__(self, values: InputParameterModel = None):
        super().__init__()
        self.values = InputParameterModel()
        self.popup = None
        self.init_window(values)

        self.lineEdit_name.textChanged.connect(self.name_changed)
        self.comboBox_param_type.currentIndexChanged.connect(self.param_type_changed)
        self.checkBox_other_size.stateChanged.connect(self.other_size_changed)
        self.checkBox_init.stateChanged.connect(self.init_changed)
        self.checkBox_parallel.stateChanged.connect(self.parallel_changed)

    def name_changed(self, text):
        self.values.set_name(text)

    def param_type_changed(self, index):
        selected_item = self.comboBox_param_type.currentText()
        self.values.set_type(selected_item)

    def parallel_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.values.set_is_parallel(True)
            return
        self.values.set_is_parallel(False)

    def init_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.values.set_init(True)
            return
        self.values.set_init(True)

    def other_size_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.values.set_is_other_size(True)
            return
        self.values.set_is_other_size(False)

    def init_window(self, values: InputParameterModel = None):
        self.setupUi(self)

        if values is not None and isinstance(values, InputParameterModel):
            self.values = values
            self.lineEdit_name.setText(self.values.get_name())

        self.show_popup_info = False
        self.checkBox_init.installEventFilter(self)
        self.checkBox_other_size.installEventFilter(self)
        self.checkBox_parallel.installEventFilter(self)

        self.comboBox_param_type.currentIndexChanged.connect(self.on_combobox_changed)

    def on_combobox_changed(self):
        current_text = self.comboBox_param_type.currentText()
        if current_text == "struct" or current_text == "struct*":
            self.struct_signal.emit(self)

    def eventFilter(self, source, event):
        if event.type() == event.Enter and self.show_popup_info:
            if source == self.checkBox_init:
                self.showPopup(
                    source,
                    "Checkbox 1",
                    "This is a description for checkbox 1 This is a description for checkbox  This is a description for checkbox  This is a description for checkbox  This is a description for checkbox ",
                )
            elif source == self.checkBox_parallel:
                self.showPopup(
                    source,
                    "Checkbox 2",
                    "This is a description for checkbox 1 This is a description for checkbox  This is a description for checkbox  This is a description for checkbox  This is a description for checkbox ",
                )
            elif source == self.checkBox_other_size:
                self.showPopup(
                    source,
                    "Checkbox 3",
                    "This is a description for checkbox 1 This is a description for checkbox  This is a description for checkbox  This is a description for checkbox  This is a description for checkbox ",
                )
        elif event.type() == event.Leave:
            if self.popup is not None:
                self.popup.close()
                self.popup = None

        return super().eventFilter(source, event)

    def showPopup(self, widget, title, description):
        pos = widget.mapToGlobal(QPoint(0, widget.height()))
        self.popup = InfoPopup(title, description, self)
        self.popup.move(pos)
        self.popup.show()
