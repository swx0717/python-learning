# import json
#
# students_score = [{"name":"张三","score":90},
#            {"name":"李四","score":80},
#            {"name":"王五","score":70}]
#
# with open("students_score.json","w",encoding="utf-8") as f:
#     json.dump(students_score,f,ensure_ascii=False,indent=2)
# print(students_score)
#
# def add_student(name, score):
#     with open("students_score.json","r",encoding="utf-8") as f:
#         students_score.append({"name":name, "score":score})
#
#     with open("students_score.json","w",encoding="utf-8") as f:
#         json.dump(students_score,f,ensure_ascii=False,indent=2)
#         return students_score
#
# def  update_score(name, new_score):
#     with open("students_score.json","r",encoding="utf-8") as f:
#         for student in students_score:
#             if student["name"] == name:
#                 student["score"] = new_score
#     with open("students_score.json","w",encoding="utf-8") as f:
#         return students_score
#
# def main(): # 加载数据
#     switch = input("输入功能：")
#     if switch == "1":
#         name = input("输入添加学生姓名：")
#         score = input("输入成绩")
#         add_student(name, score)
#
#     if switch == "2":
#         name = input("输入修改成绩的学生姓名：")
#         new_score = input("输入修改的成绩:")
#         update_score(name, new_score)
#
#
# if __name__ == "__main__":
#     main()
import json

STUDENTS_FILE = "students_score.json"

def load_students():
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # 默认数据
        default = [{"name": "张三", "score": 90}, {"name": "李四", "score": 80}, {"name": "王五", "score": 70}]
        save_students(default)  # 自动保存默认数据
        return default

def save_students(students):
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def add_student(students, name, score):
    students.append({"name": name, "score": score})
    save_students(students)

def update_score(students, name, new_score):
    for student in students:
        if student["name"] == name:
            student["score"] = new_score
            save_students(students)
            return True
    return False

def main():
    students = load_students()   # 加载数据
    while True:
        print("\n1. 添加学生")
        print("2. 修改成绩")
        print("3. 退出")
        choice = input("请选择：")
        if choice == "1":
            name = input("姓名：")
            score = int(input("成绩："))   # 转换整数
            add_student(students, name, score)
            print("添加成功")
        elif choice == "2":
            name = input("姓名：")
            new_score = int(input("新成绩："))
            if update_score(students, name, new_score):
                print("修改成功")
            else:
                print("未找到该学生")
        elif choice == "3":
            break
        else:
            print("无效选项")


if __name__ == "__main__":
    main()