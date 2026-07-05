with open("poem.txt", "w", encoding="utf-8") as file:
    file.write("学习文件操作01")

with open("poem.txt", "a", encoding="utf-8") as file:
    file.write("\n好好学习，天天向上")

with open("poem.txt", "r", encoding="utf-8") as f:
    whole = f.read()
    print(whole)

with open("poem.txt", "r", encoding="utf-8") as f:
    first5 = f.read(5)
    print(first5)

with open("poem.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1,end='')
    print(line2,end='')

# with open("poem.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         process(line)


