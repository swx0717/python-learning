import json
# {
#     "name":"Alice",
#     "age":20,
#     "courses":["Math","Physics"],
#     "score":95.5
# }

data = {"name":"Bob","age":25}
with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f)

print(data)

with open("data.json","r",encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)
print(type(loaded))

data = {"姓名": "张三", "年龄": 30}
with open("chinese.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False)

data= {"name": "Alice", "scores": [90, 85, 92]}
with open("pretty.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)
