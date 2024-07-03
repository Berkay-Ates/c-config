class OutputParameterModel:

    def __init__(self, type: str = "int", name: str = ""):
        self._type = type
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        if not type in ["int", "int*", "float", "float*", "double", "double*"]:
            raise ValueError("type must be [int,int*,float,float*,double,double*]")
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self._name = name

    def __str__(self):
        return f"OutputParameterModel(type={self._type}, name='{self._name}')"
