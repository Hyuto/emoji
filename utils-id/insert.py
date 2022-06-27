import json


with open("result.json") as reader:
    emoji_data = json.load(reader)

indo = [emoji_data[x]["id"].lower() for x in emoji_data if "it" in emoji_data[x].keys()]

with open("emoji/unicode_codes/data_dict.py") as reader:
    script = reader.readlines()[44:]

result = []

index = 0
for line in script:
    if "'it': u'" in line:
        result.append(line.replace("\n", "") + ",\n")
        result.append(f"        'id': u'{indo[index]}'\n")
        index += 1
    else:
        result.append(line)

with open("baru.py", "w") as writer:
    writer.write("".join(result))
