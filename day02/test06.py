date = int(input("输入年份："))
if date % 4 == 0 or date % 100 == 0 or date % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")