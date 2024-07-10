class InputParameterModel:

    def __init__(
        self,
        type: str = "int",
        name: str = "",
        is_parallel: bool = False,
        is_other_size: bool = False,
        is_init: bool = False,
    ):
        self.type_ = type
        self.name_ = name
        self.is_parallel_ = is_parallel
        self.is_other_size_ = is_other_size
        self.is_init_ = is_init

    def set_type(self, type):
        self.type_ = type

    def set_name(self, name):
        self.name_ = name

    def set_is_parallel(self, parallel):
        self.is_parallel_ = parallel

    def set_is_other_size(self, other_size):
        self.is_other_size_ = other_size

    def set_init(self, init):
        self.is_init_ = init

    def get_type(self):
        return self.type_

    def get_name(self):
        return self.name_

    def get_is_parallel(self):
        return self.is_parallel_

    def get_is_other_size(self):
        return self.is_other_size_

    def get_init(self):
        return self.is_init_

    def __str__(self):
        return (
            f"InputParameterModel(type={self.type_}, name='{self.name_}', "
            f"is_parallel={self.is_parallel_}, is_other_size={self.is_other_size_}, "
            f"is_init={self.is_init_})"
        )

    def to_dict(self):
        return {
            "type_": self.type_,
            "name_": self.name_,
            "is_parallel_": self.is_parallel_,
            "is_other_size_": self.is_other_size_,
            "is_init_": self.is_init_,
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            type=dict_obj.get("type_", "int"),
            name=dict_obj.get("name_", ""),
            is_parallel=dict_obj.get("is_parallel_", False),
            is_other_size=dict_obj.get("is_other_size_", False),
            is_init=dict_obj.get("is_init_", False),
        )
