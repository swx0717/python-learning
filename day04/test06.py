# student = [
#     {"name" : "张三","age" : "19","city" : "北京"},
#     {"name" : "李四","age" : "21","city" : "南京"},
# ]
#转化整数列表
students = {
    "张三": 85,
    "李四": 72,
    "王五": 59,
    "小王": 40,
    "刘羊": 59,
}
name = input("查询名称：")
if name in students:
    print(f"{name}:{students[name]}")
students.update({"小明":90})
print(students)
students["王五"] = 95
print(students)
del students["李四"]
print(students)
print(list(students.items()))
top_name = max(students, key=students.get)
print(f"最高分学生：{top_name},分数：{students[top_name]}")
for key, value in students.items():
    if value < 60:
        print(f"{key}:{value}")
else:
    print("没有不及格的学生")