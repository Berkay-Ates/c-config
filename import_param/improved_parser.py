import re
import json


def parse_struct_body(struct_body):
    input_parameters = []
    output_parameters = []
    current_section = None
    inner_structs = []

    lines = struct_body.splitlines()
    for line in lines:
        line = line.strip()
        if line:
            if line.startswith("// input parameters"):
                current_section = "input_parameters"
            elif line.startswith("// output parameters"):
                current_section = "output_parameters"
            else:
                member_pattern = re.compile(r"(\w+)\s+(\w+);")
                member_match = member_pattern.match(line)
                struct_pattern = re.compile(r"(\w+)\s+(\w+);")
                struct_match = struct_pattern.match(line)
                if member_match and current_section:
                    member_type = member_match.group(1)
                    member_name = member_match.group(2)
                    param_info = {
                        "type_": member_type,
                        "name_": member_name,
                        "is_parallel_": False,
                        "is_other_size_": False,
                        "is_init_": False,
                    }
                    if current_section == "input_parameters":
                        input_parameters.append(param_info)
                    else:
                        output_parameters.append(param_info)
                elif struct_match:
                    struct_name = struct_match.group(1)
                    inner_structs.append(struct_name)
    return input_parameters, output_parameters, inner_structs


def parse_header_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    structs = {}

    struct_pattern = re.compile(r"struct\s+(\w+)\s*{([^}]*)}", re.DOTALL)
    matches = struct_pattern.findall(content)

    for match in matches:
        struct_name = match[0]
        struct_body = match[1].strip()
        input_parameters, output_parameters, inner_structs = parse_struct_body(struct_body)

        structs[struct_name] = {
            "input_parameters": input_parameters,
            "output_parameters": output_parameters,
            "inner_structs": inner_structs,
        }

    return structs


def build_json_model(struct_name, structs_info):
    struct_info = structs_info[struct_name]
    input_parameter_models = struct_info["input_parameters"]
    input_struct_parameter_models = []

    for inner_struct_name in struct_info["inner_structs"]:
        input_struct_parameter_models.append(build_json_model(inner_struct_name, structs_info))

    return {
        "type": "str",
        "name": struct_name,
        "input_parameter_models": input_parameter_models,
        "input_struct_parameter_models": input_struct_parameter_models,
    }


def generate_json_model(structs_info):
    top_level_structs = [
        k for k, v in structs_info.items() if not any(k in vs["inner_structs"] for vs in structs_info.values())
    ]
    json_model = {"name": "Algorithm", "input_parameter_models": [], "input_struct_parameter_models": []}
    for struct_name in top_level_structs:
        json_model["input_struct_parameter_models"].append(build_json_model(struct_name, structs_info))
    return json_model


# Test etmek için örnek header dosyası yolunu belirtin
header_file_path = "complex_example.h"
structs_info = parse_header_file(header_file_path)
json_model = generate_json_model(structs_info)

# JSON modelini ekranda gösterme
print(json.dumps(json_model, indent=4))

# JSON dosyasına kaydetme
with open("structs_info2.json", "w") as json_file:
    json.dump(json_model, json_file, indent=4)
