from PyQt5.QtWidgets import *
from ui_py_files import StructParameterWidget
from .input_param_controller import InputParameterController
from typing import List
from models import InputStructureModel


class StructParameterController(QWidget, StructParameterWidget):

    def __init__(self):
        super().__init__()
        self.values = InputStructureModel()
        self.init_window()

    def init_window(self):
        self.setupUi(self)
        self.pushButton_add_struct_param.clicked.connect(self.add_item)
        self.pushButton_remove_struct_item.clicked.connect(self.remove_item)

        self.lineEdit_struct_name.textChanged.connect(self.struct_name_changed)
        self.comboBox_struct_type.currentIndexChanged.connect(self.struct_type_changed)

    def struct_type_changed(self):
        self.values.type = self.comboBox_struct_type.currentText()

    def struct_name_changed(self, text):
        self.values.name = text

    def add_struct(self, input_param_controller: InputParameterController):
        print("Struct Adding.....")
        # delete changed struct from the list
        for index in range(self.listWidget_struct_parameters.count()):
            item = self.listWidget_struct_parameters.item(index)
            if item is not None:
                widget = self.listWidget_struct_parameters.itemWidget(item)
                if widget == input_param_controller:
                    self.listWidget_struct_parameters.takeItem(index)
                    self.values.remove_input_parameter_model(input_param_controller)
                    widget.deleteLater()
                    break
        self.add_struct_func()

    def add_struct_func(self):

        new_widget = StructParameterController()
        new_item = QListWidgetItem(self.listWidget_struct_parameters)
        new_item.setSizeHint(new_widget.sizeHint())

        self.listWidget_struct_parameters.addItem(new_item)
        self.listWidget_struct_parameters.setItemWidget(new_item, new_widget)

        self.values.add_input_struct_parameter_model(new_widget)

        print(f"input param:{len(self.values.get_input_parameter_models())}")
        print(f"input struct:{len(self.values.get_input_struct_parameter_models())}")
        for i in self.values.get_input_struct_parameter_models():
            print((i.values))

    def add_item(self):
        # Create an instance of your custom widget
        custom_widget = InputParameterController()
        self.values.add_input_parameter_model(custom_widget)
        custom_widget.struct_signal.connect(self.add_struct)
        self.label_parameter_count.setText(f"Parameter Count: {len(self.values.get_input_parameter_models())}")

        # Create a QListWidgetItem
        item = QListWidgetItem(self.listWidget_struct_parameters)

        # Set the size hint of the item to match the custom widget's size
        item.setSizeHint(custom_widget.sizeHint())

        # Add the item to the list widget
        self.listWidget_struct_parameters.addItem(item)

        # Set the custom widget as the item widget in the list widget
        self.listWidget_struct_parameters.setItemWidget(item, custom_widget)
        for item in self.values.get_input_parameter_models():
            print(item.values)

    def remove_item(self):
        list_widget = self.listWidget_struct_parameters  # Assuming you are deleting from output list

        selected_items = list_widget.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "No Selection", "Please select an item to remove.")
            return  # If no item is selected, do nothing

        selected_items = selected_items[0]

        index = list_widget.row(selected_items)
        custom_widget = list_widget.itemWidget(selected_items)

        # Remove from list
        if custom_widget in self.values.get_input_parameter_models():
            self.values.remove_input_parameter_model(custom_widget)
        elif custom_widget in self.values.get_input_struct_parameter_models():
            self.values.remove_input_struct_parameter_model(custom_widget)

        # Remove from list widget
        list_widget.takeItem(index)

        # Optionally, delete the custom widget (if needed)
        custom_widget.deleteLater()

        # Update display
        self.label_parameter_count.setText(f"Parameter Count: {len(self.values.get_input_parameter_models())}")
