# sentence = input("输入一个英语句子(间隔用空格):")
# sentence = sentence.split()
# print(sentence)
# print(len(sentence))

while True:
    numbers = input("输入电话号码")
    if len(numbers) == 11:
        new_numbers = numbers[0:3]+"****"+numbers[7:]
        print(new_numbers)
        numbers = list(numbers)
        print(numbers)
        numbers[3:7] = ["*","*","*","*"]
        hidden = "".join(numbers)
        print(hidden)
        break
    else:
        print("输入正确的电话号码")