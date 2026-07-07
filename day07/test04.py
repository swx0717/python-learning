import json

STUDENTS_FILE = "students.json"

def load_students():
    try:
        with open(STUDENTS_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        return []

def save_students(students):
    with open(STUDENTS_FILE,"w",encoding="utf-8") as f:
        json.dump(students,f,ensure_ascii=False,indent=4)

students = load_students()

def add_student(name,score):
    students.append({"name":name,"score":score})
    save_students(students)

def update_student(name,score):
    for s in students:
        if s["name"] == name:
            s["score"] = score
            save_students(students)
            return True
    return False

def delete_student(name):
    global students
    students = [s for s in students if s["name"] != name]
    save_students(students)

students = load_students()
if not students:
    add_student("Alice", 90)
    add_student("Bob", 85)
    add_student("Charlie", 88)
    print("已添加3个学生")
else:
    print("已加载已有数据")

update_student("Bob", 90)
print("Bob的成绩修改为了95")

print("当前所有学生:")
for s in students:
    print(f"{s['name']},{s['score']}")