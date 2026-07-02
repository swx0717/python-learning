# import random
# def game():
#     target = random.randint(1,100)
#     count = 0
#     max_times = 7
#     print("===猜数字===")
#     print(f"系统已生成1-100数字，你有{max_times}次机会")
#     while count < max_times:
#         s = input("输入数字")
#         if not s.isdigit():
#             print("输入不合法")
#             continue
#         guess = int(s)
#         count += 1
#         if guess > target:
#            print(f"大了，还剩{max_times - count}次机会")
#         elif guess < target:
#            print(f"猜小了！还剩{max_times - count}次机会")
#         else:
#            print(f"恭喜猜对了！一共使用了{count}次")
#            break
#     else:
#         print(f"机会用完了，正确数字是{target}")
# while True:
#     game()
#     again = input("是否继续？输入y继续，其他退出：")
#     if again != "y":
#         print("游戏结束")
#         break

scores = []
while True:
    score = float(input("输入成绩（-1结束）："))
    if score == -1:
        break
    scores.append(score)
if scores:
    total = len(scores)
    print(f"总人数:{total}")
    print(f"平均分：{round(sum(scores)/total,2)}")
    print(f"最高分：{max(scores)}")
    print(f"最低分：{min(scores)}")
    pass_list = []
    for score in scores:
        if score >= 60 :
            pass_list.append(score)
    print(f"及格人数：{len(pass_list)}")
    print(f"不及格人数：{total-len(pass_list)}")
else:
    print("无效成绩")