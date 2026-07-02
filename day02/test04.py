
number_1 = float(input("第一个数："))
number_2 = float(input("第二个数："))
number_3 = float(input("第三个数："))
if number_1 >= number_2 and number_1 >= number_3:
    print(f"最大值：{number_1}")
elif number_2 >= number_1 and number_2 >= number_3:
    print(f"最大值：{number_2}")
else:
    print(f"最大值：{number_3}")