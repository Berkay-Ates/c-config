from PyQt5.QtWidgets import *
from ui_py_files import StructParameterWidget
from .input_param_controller import InputParameterController
from typing import List


class StructParameterController(QWidget, StructParameterWidget):

    def __init__(self):
        super().__init__()
        self.input_parameters: List[InputParameterController] = []
        self.init_window()

    def init_window(self):
        self.setupUi(self)
        self.pushButton_add_struct_param.clicked.connect(self.add_item)
        self.pushButton_remove_struct_item.clicked.connect(self.remove_item)

    def add_item(self):

        # Create an instance of your custom widget
        custom_widget = InputParameterController()
        self.input_parameters.append(custom_widget)
        self.label_parameter_count.setText(f"Parameter Count: {len(self.input_parameters)}")

        # Create a QListWidgetItem
        item = QListWidgetItem(self.listWidget_struct_parameters)

        # Set the size hint of the item to match the custom widget's size
        item.setSizeHint(custom_widget.sizeHint())

        # Add the item to the list widget
        self.listWidget_struct_parameters.addItem(item)

        # Set the custom widget as the item widget in the list widget
        self.listWidget_struct_parameters.setItemWidget(item, custom_widget)
        for item in self.input_parameters:
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
        self.input_parameters.remove(custom_widget)

        # Remove from list widget
        list_widget.takeItem(index)

        # Optionally, delete the custom widget (if needed)
        custom_widget.deleteLater()

        # Update display
        self.label_parameter_count.setText(f"Parameter Count: {len(self.input_parameters)}")
