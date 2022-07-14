import json


AccountData = {
    "people": ""
}


username = input("enter username")
password = input("enter password")

AccountData.update({"username": username})
AccountData.update({"password": password})


with open("json.json", "w") as f:
    json.dump(AccountData, f, indent=2)
f.close()

with open("json2.json") as f:
    data = json.load(f)

print(data)

for account in data["accounts"]:
    print(account["password"])
