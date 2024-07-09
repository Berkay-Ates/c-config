from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, QObject, pyqtSignal
from ui_py_files import InputParameterWidget
from models import InputParameterModel
from ui_py_files import InfoPopup


class InputParameterController(QWidget, InputParameterWidget):

    struct_signal = pyqtSignal(QObject)

    def __init__(self):
        super().__init__()
        self.values = InputParameterModel()
        self.popup = None
        self.init_window()

    def init_window(self):
        self.setupUi(self)

        self.show_popup_info = False
        self.checkBox.installEventFilter(self)
        self.checkBox_2.installEventFilter(self)
        self.checkBox_3.installEventFilter(self)

        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)

    def on_combobox_changed(self):
        current_text = self.comboBox.currentText()
        if current_text == "struct" or current_text == "struct*":
            self.struct_signal.emit(self)

    def eventFilter(self, source, event):
        if event.type() == event.Enter and self.show_popup_info:
            if source == self.checkBox:
                self.showPopup(
                    source,
                    "Checkbox 1",
                    "This is a description for checkbox 1 This is a description for checkbox  This is a description for checkbox  This is a description for checkbox  This is a description for checkbox ",
                )
            elif source == self.checkBox_2:
                self.showPopup(
                    source,
                    "Checkbox 2",
                    "This is a description for checkbox 1 This is a description for checkbox  This is a description for checkbox  This is a description for checkbox  This is a description for checkbox ",
                )
            elif source == self.checkBox_3:
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
