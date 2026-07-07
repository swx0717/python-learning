import json

student = {"id": 1, "name": "Tom", "grade": 88}
with open("student.json","w",encoding="utf-8") as f:
    json.dump(student,f,ensure_ascii=False,indent=4)

with open("student.json","r",encoding="utf-8") as f:
    student = json.load(f)
print(student["name"])

students = [{"name": "Alice"}, {"name": "Bob"}]
with open("student.json","w",encoding="utf-8") as f:
    json.dump(students,f,ensure_ascii=False,indent=4)

with open("student.json","r",encoding="utf-8") as f:
    data = json.load(f)

data.append({"name": "charlie"})

with open("student.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

data = {"课程":"Python","人数":30}
with open("course.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

