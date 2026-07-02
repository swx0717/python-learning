# number_one = float(input("输入第一个数字："))
# operator = input("输入运算符：")
# number_two = float(input("输入第二个数："))
# if operator == "+":
#     print(round(number_one * number_two,2))
# elif operator == "-":
#     print(round(number_one * number_two,2))
# elif operator == "*":
#     print(round(number_one * number_two,2))
# elif operator == "/" and number_two !=0:
#     print(round(number_one / number_two,2))
# elif operator == "/" and number_two ==0:
#     print("除数为0")
# else:
#     print("不支持运算符")

price = float(50)
age = int(input("输入年龄："))
vip = input("是否是会员（输入：是/不是）：")
if vip == "是":
    if age <12 :
        money = price*0.5 - 5
    elif age >60:
        money = price*0.7 - 5
    else:
        money = price - 5

if vip == "不是":
    if age <12 :
        money = price*0.5
    elif age >60:
        money = price*0.7
    else:
        money = price
print(money)



