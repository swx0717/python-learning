#test01
name = input("商品名称：")
price = float(input("输入单价："))
number = int(input("购买数量："))
money = price * number
if money > 100:
    money = money*0.9
print(f"总价：{round(money,2)}")