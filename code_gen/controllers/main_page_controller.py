from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ui_py_files import MainWindow
from PyQt5.QtGui import QPixmap
from .output_param_controller import OutputParameterController
from .input_param_controller import InputParameterController
from .struct_parameter_widget import StructParameterController
from utils import check_java_installed, check_doxygen_installed, PopUpWindows, text
from typing import List
import json


class MainWindowController(QMainWindow, MainWindow):

    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.setupUi(self)
        self.pushButton_add_output_parameter.clicked.connect(self.add_output_item)
        self.pushButton_add_input_parameters.clicked.connect(self.add_input_item)
        self.horizontalSlider_core_count.valueChanged.connect(self.on_slider_change)
        self.pushButton_delete_output_param.clicked.connect(self.delete_selected_params)
        self.pushButton_delete_input_parameters.clicked.connect(self.delete_selected_input_param)
        self.pushButton_get_diagram.clicked.connect(self.get_diagram)
        self.checkBox_show_popup_messages.stateChanged.connect(self.show_popup_changed)
        self.pushButton_generate_code.clicked.connect(self.generate_code)
        self.pushButton_get_readme.clicked.connect(self.get_readme_text)
        self.pushButton_add_struct.clicked.connect(self.add_struct)

        self.pushButton_import.clicked.connect(self.import_button_clicked)

        # parameters
        self.input_parameters: List[InputParameterController] = []
        self.output_parameters: List[OutputParameterController] = []
        self.input_struct_parameters = []

        print("*****************", len(self.output_parameters))

    def import_button_clicked(self):
        json_list = []
        for item in self.input_parameters:
            json_list.append(item.values.__dict__)

        print(json_list)

        with open("objects.json", "w") as json_file:
            json.dump(json_list, json_file, indent=4)

    def get_readme_text(self):
        self.plainTextEdit.setPlainText(text)

    def generate_code(self):
        if not check_doxygen_installed():
            result = PopUpWindows.notification_message(
                "you have't got doxygen installed, do you want to generate code without doxygen documentation"
            )
            if not result:
                return
        if not check_java_installed():
            result = PopUpWindows.notification_message(
                "you have't got doxygen installed, do you want to generate code without doxygen documentation"
            )
            if not result:
                return

        print("Generating the code...")

    def show_popup_changed(self, state):
        if state == Qt.Checked:
            for input_controller in self.input_parameters:
                input_controller.show_popup_info = True
        else:
            for input_controller in self.input_parameters:
                input_controller.show_popup_info = False

    def get_diagram(self):
        if not check_java_installed():
            PopUpWindows.show_error_message("First you have to install jave!")
            return
        # Önceki diagramları temizle
        for i in reversed(range(self.verticalLayout_class_diagram.count())):
            widget = self.verticalLayout_class_diagram.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        label_image = QLabel(self)
        pixmap = QPixmap("C:\\Users\\atesb\Desktop\\cpp_config\\code_gen\\image.png")
        scaled_pixmap = pixmap.scaled(self.groupBox_class_diagram.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_image.setPixmap(scaled_pixmap)
        self.verticalLayout_class_diagram.addWidget(label_image)

    def delete_selected_input_param(self):
        list_widget = self.listWidget_input_parameters

        selected_items = list_widget.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "No Selection", "Please select an item to remove.")
            return  # If no item is selected, do nothing

        selected_items = selected_items[0]

        index = list_widget.row(selected_items)
        custom_widget = list_widget.itemWidget(selected_items)

        # Remove from list
        if custom_widget in self.input_struct_parameters:
            self.input_struct_parameters.remove(custom_widget)
        else:
            self.input_parameters.remove(custom_widget)

        # Remove from list widget
        list_widget.takeItem(index)

        # Optionally, delete the custom widget (if needed)
        custom_widget.deleteLater()

    def delete_selected_params(self):
        list_widget = self.listWidget_output_parameters  # Assuming you are deleting from output list

        selected_items = list_widget.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "No Selection", "Please select an item to remove.")
            return  # If no item is selected, do nothing

        selected_items = selected_items[0]

        index = list_widget.row(selected_items)
        custom_widget = list_widget.itemWidget(selected_items)

        # Remove from list
        self.output_parameters.remove(custom_widget)

        # Remove from list widget
        list_widget.takeItem(index)

        # Optionally, delete the custom widget (if needed)
        custom_widget.deleteLater()

        # Update display
        self.label_output_parameters.setText(f"Output Parameters: {len(self.output_parameters)}")

    def on_slider_change(self, value):
        self.label_core_count.setText(f"Core count: {value}")

    def add_output_item(self):
        # Create an instance of your custom widget
        custom_widget = OutputParameterController()
        self.output_parameters.append(custom_widget)
        self.label_output_parameters.setText(f"Output Parameters: {len(self.output_parameters)}")

        for item in self.output_parameters:
            print(item.values)

        # Create a QListWidgetItem
        item = QListWidgetItem(self.listWidget_output_parameters)

        # Set the size hint of the item to match the custom widget's size
        item.setSizeHint(custom_widget.sizeHint())

        # Add the item to the list widget
        self.listWidget_output_parameters.addItem(item)

        # Set the custom widget as the item widget in the list widget
        self.listWidget_output_parameters.setItemWidget(item, custom_widget)

    def add_struct(self):

        new_widget = StructParameterController()
        new_item = QListWidgetItem(self.listWidget_input_parameters)
        new_item.setSizeHint(new_widget.sizeHint())

        self.listWidget_input_parameters.addItem(new_item)
        self.listWidget_input_parameters.setItemWidget(new_item, new_widget)

        self.input_struct_parameters.append(new_widget)

        print(f"input param:{len(self.input_parameters)}")
        print(f"input struct:{len(self.input_struct_parameters)}")
        for i in self.input_parameters:
            print((i.values))

    def struct_adding(self, input_param_controller: InputParameterController):
        print("Struct Adding.....")
        # delete changed struct from the list
        for index in range(self.listWidget_input_parameters.count()):
            item = self.listWidget_input_parameters.item(index)
            if item is not None:
                widget = self.listWidget_input_parameters.itemWidget(item)
                if widget == input_param_controller:
                    self.listWidget_input_parameters.takeItem(index)
                    self.input_parameters.remove(input_param_controller)
                    widget.deleteLater()
                    break

        self.add_struct()

        print(f"input_params:{ len(self.input_parameters)}")
        print(f"input_structs:{ len(self.input_struct_parameters)}")

    def add_input_item(self):
        # Create an instance of your custom widget
        custom_widget = InputParameterController()
        self.input_parameters.append(custom_widget)
        custom_widget.struct_signal.connect(self.struct_adding)
        self.label_input_parameters.setText(f"Input Parameters: {len(self.input_parameters)}")

        # Create a QListWidgetItem
        item = QListWidgetItem(self.listWidget_input_parameters)

        # Set the size hint of the item to match the custom widget's size
        item.setSizeHint(custom_widget.sizeHint())

        # Add the item to the list widget
        self.listWidget_input_parameters.addItem(item)

        # Set the custom widget as the item widget in the list widget
        self.listWidget_input_parameters.setItemWidget(item, custom_widget)
