import re
import json


def parse_struct_body(struct_body):
    members = {"input_parameters": [], "output_parameters": []}
    current_section = None

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
                if member_match and current_section:
                    member_type = member_match.group(1)
                    member_name = member_match.group(2)
                    members[current_section].append({"type": member_type, "name": member_name})
    return members


def parse_header_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    structs = {}

    struct_pattern = re.compile(r"struct\s+(\w+)\s*{([^}]*)}", re.DOTALL)
    matches = struct_pattern.findall(content)

    for match in matches:
        struct_name = match[0]
        struct_body = match[1].strip()
        members = parse_struct_body(struct_body)
        structs[struct_name] = members

        # İç içe struct'ları bulmak için struct body içinde tekrar arama yap
        inner_matches = struct_pattern.findall(struct_body)
        for inner_match in inner_matches:
            inner_struct_name = inner_match[0]
            inner_struct_body = inner_match[1].strip()
            inner_members = parse_struct_body(inner_struct_body)
            structs[inner_struct_name] = inner_members

    return structs


# Test etmek için örnek header dosyası yolunu belirtin
header_file_path = "complex_example.h"
structs_info = parse_header_file(header_file_path)

# Struct bilgilerini ekranda gösterme
for struct_name, sections in structs_info.items():
    print(f"Struct: {struct_name}")
    for section_name, members in sections.items():
        print(f"  {section_name}:")
        for member in members:
            print(f"    {member['type']} {member['name']}")

# JSON dosyasına kaydetme
with open("structs_info.json", "w") as json_file:
    json.dump(structs_info, json_file, indent=4)
