import os

# file = open("notes.txt","w",encoding="utf-8")
# file.write("学习文件操作")
# file.close()
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("今天开始学习文件操作")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\n第二条内容")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
#
# print(content)
#
# line = file.readline()
# print(line)

print(os.getcwd())

file1 = "data/input.txt"
file2 = "../logs/erroe.log"

file3 = r"F:\python_AI\day06\report.txt"

f = open("notes.txt","r")

f = open("new.txt","w")

f = open("notes.txt","a")

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
