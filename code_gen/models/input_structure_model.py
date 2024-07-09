from ui_py_files import InputParameterWidget
from ui_py_files import StructParameterWidget


class InputStructureModel:

    def __init__(self, type: str = "str", name: str = ""):
        self._type = type
        self._name = name
        self._input_parameter_models = []
        self._input_struct_parameter_models = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        if not type in ["str", "str*"]:
            raise ValueError("type must be [str, str*]")
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self._name = name

    def add_input_struct_parameter_model(self, input_struct_parameter_model):
        if not isinstance(input_struct_parameter_model, StructParameterWidget):
            raise ValueError("input_struct_parameter_model must be an instance of InputStructParameterModel")
        self._input_struct_parameter_models.append(input_struct_parameter_model)

    def remove_input_struct_parameter_model(self, input_struct_parameter_model):
        if input_struct_parameter_model in self._input_struct_parameter_models:
            self._input_struct_parameter_models.remove(input_struct_parameter_model)

    def get_input_struct_parameter_models(self):
        return self._input_struct_parameter_models

    def add_input_parameter_model(self, input_parameter_model: InputParameterWidget):
        if not isinstance(input_parameter_model, InputParameterWidget):
            raise ValueError("input_parameter_model must be an instance of InputParameterModel")
        self._input_parameter_models.append(input_parameter_model)

    def remove_input_parameter_model(self, input_parameter_model: InputParameterWidget):
        if input_parameter_model in self._input_parameter_models:
            self._input_parameter_models.remove(input_parameter_model)

    def get_input_parameter_models(self):
        return self._input_parameter_models

    def __str__(self):
        return f"OutputParameterModel(type={self._type}, name='{self._name}')"
