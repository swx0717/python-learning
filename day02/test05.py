grade = float(input("成绩："))
if 90<= grade <= 100:
    print("优秀")
elif 80<=grade<=90:
    print("良好")
elif 60<=grade<=80:
    print("一般")
elif grade<0 or grade >100:
    print("输入正确成绩")
else:
    print("不及格")