s = input("请输入字符串")
s = s.lower()
s_list_2 = s.split(" ")
print(s_list_2)
s = s.replace(" ","")
print(s)
s_list = list(s)
s_list_1 = list(reversed(s_list))
if s_list_1 == s_list:
    print("是回文")
else:
    print("不是回文")