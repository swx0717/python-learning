import json

person = {"name": "Alice", "age": 30, "city": "Beijing"}

with open("person.json","w",encoding="utf-8") as f:
    json.dump(person,f,ensure_ascii=False,indent=2)

print(person)


fruits = ["apple", "banana", "cherry"]

with open("fruit.json","w",encoding="utf-8") as f:
    json.dump(fruits,f,ensure_ascii=False,indent=2)

with open("fruit.json","r",encoding="utf-8") as f:
    data = json.load(f)
    print(data[1])

with open("person.json","r",encoding="utf-8") as f:
    person = json.load(f)
    person["name"] = "Alice"
    person["age"] = 31
    person["city"] = "Shanghai"

with open("person.json","w",encoding="utf-8") as f:
    json.dump(person,f,ensure_ascii=False,indent=4)
    