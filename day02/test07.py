USERNAME = "admin"
PASSWORD = "123456"
username = input("输入用户名：")
password = input("输入密码：")
if username == USERNAME and password == PASSWORD:
    print("登陆成功")
else:
    print("验证失败")