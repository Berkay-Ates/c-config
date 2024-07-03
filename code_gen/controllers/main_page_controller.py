from PyQt5.QtWidgets import *
import sys
from ui_py_files import MainWindow
from .output_param_controller import OutputParameterController
from .input_param_controller import InputParameterController


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

        # parameters
        self.input_parameters = []
        self.output_parameters = []

        print("*****************", len(self.output_parameters))

    def delete_selected_params(self):
        list_widget = self.listWidget_output_parameters  # Assuming you are deleting from output list

        selected_items = list_widget.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "No Selection", "Please select an item to remove.")
            return  # If no item is selected, do nothing

        for item in selected_items:
            index = list_widget.row(item)
            custom_widget = list_widget.itemWidget(item)

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

    def add_input_item(self):
        # Create an instance of your custom widget
        custom_widget = InputParameterController()
        self.input_parameters.append(custom_widget)
        self.label_input_parameters.setText(f"Input Parameters: {len(self.input_parameters)}")

        # Create a QListWidgetItem
        item = QListWidgetItem(self.listWidget_input_parameters)

        # Set the size hint of the item to match the custom widget's size
        item.setSizeHint(custom_widget.sizeHint())

        # Add the item to the list widget
        self.listWidget_input_parameters.addItem(item)

        # Set the custom widget as the item widget in the list widget
        self.listWidget_input_parameters.setItemWidget(item, custom_widget)
