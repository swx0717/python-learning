#转化整数列表
numbers = input("输入一串数字（用空格隔开）：")
numbers = numbers.split()
numbers_list = [int(num) for num in numbers]
#最大最小值
print(max(numbers_list))
print(min(numbers_list))
#平均值
sum = 0
scores_1 = []
scores_2 = []
for number in numbers_list:
    sum += number
print(round(sum/len(numbers_list),2))
#找不不及格成绩
for number in numbers_list:
    if 60 <= number <= 100:
        scores_1.append(number)
    elif 0 <=number < 60 :
        scores_2.append(number)
    else:
        print("请输入正确的成绩")
print(scores_1)
print(scores_2)
#排序
numbers_list.sort()
print(numbers_list)
#去重
seen = []
for i in numbers:
    if i not in seen:
        seen.append(i)
print(seen)
#大于平均分的成绩
seen_1 = []
for number in numbers_list:
    if number > round(sum/len(numbers_list),2):
        seen_1.append(number)
print(seen_1)
