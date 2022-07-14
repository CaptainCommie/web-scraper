import json

with open("json.json") as f:
    data = json.load(f)

for people in data["people"]:
    age = people["age"]
    new_age = age + 1
    people["age"] = new_age

with open("json.json", "w") as f:
    json.dump(data, f, indent=2)



