from ui_py_files import InputParameterWidget
from .input_parameter_model import InputParameterModel

from ui_py_files import StructParameterWidget
from typing import List, Dict


class InputStructureModel:

    def __init__(self, type: str = "str", name: str = ""):
        self._type = type
        self._name = name
        self._input_parameter_models: List[InputParameterWidget] = []
        self._input_struct_parameter_models: List[StructParameterWidget] = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        if not type in ["struct", "struct*"]:
            raise ValueError("type must be [struct, struct*]")
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
        return f"OutputParameterModel(type={self._type}, name='{self._name}',input_parameter_len:{len(self._input_parameter_models)},input_struct_len={len(self._input_struct_parameter_models)} )"

    def to_dict(self) -> Dict[str, any]:
        return {
            "type": self._type,
            "name": self._name,
            "input_parameter_models": [model.values.to_dict() for model in self._input_parameter_models],
            "input_struct_parameter_models": [model.values.to_dict() for model in self._input_struct_parameter_models],
        }

    @classmethod
    def from_dict(cls, dict_obj: Dict[str, any]):
        obj = cls(type=dict_obj.get("type", "str"), name=dict_obj.get("name", ""))
        obj._input_parameter_models = [
            InputParameterModel.from_dict(m) for m in dict_obj.get("input_parameter_models", [])
        ]
        obj._input_struct_parameter_models = [
            cls.from_dict(m) for m in dict_obj.get("input_struct_parameter_models", [])
        ]
        return obj
