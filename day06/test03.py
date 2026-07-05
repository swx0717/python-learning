lines = ("Alice,20\nBob,22\nCharlie,21")
with open("students.txt","w", encoding="utf-8") as file:
    file.writelines(lines)

total_age = 0
count = 0

with open("students.txt","r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            name,age = line.split(",",1)
            total_age += int(age)
            count = count + 1

avg_age = total_age/count if count > 0 else 0

with open("result.txt","w", encoding="utf-8") as file:
    file.write(f"学生总数：{count}\n")
    file.write(f"平均年龄：{avg_age}\n")

with open("result.txt","r", encoding="utf-8") as file:
    # whole = file.read()
    # print(whole)
    print(file.read())