number = int(input("输入一个整数:"))
res = 0   # 存放反转后的数字
sum_digit = 0  # 存放各位数字和
temp = number

while temp > 0:
    digit = temp % 10        # 取出最后一位
    res = res * 10 + digit   # 拼接反转数
    sum_digit += digit       # 累加每一位
    temp = temp // 10        # 去掉最后一位，只写一次

print("反转后的数字：", res)
print("各位数字之和：", sum_digit)