def add_lines():
    content = input("输入日志内容：")
    with open("result.txt","a", encoding="utf-8") as file:
        file.writelines(content + "\n")
    print("添加成功")

def read_lines():
    with open("result.txt","r", encoding="utf-8") as file:
        # whole = file.read()
        # print(whole)
        for line in file:
            print(line.strip())

def count_lines():
    with open("result.txt","r", encoding="utf-8") as file:
        count = 0
        for line in file:
            line = line.strip()
            new_line = line.split("\n")
            count += 1
        print(count)

def find_line(lines):
    try:
        found = False
        with open("result.txt","r", encoding="utf-8") as file:
            # for line in file:
            #     line = line.strip()
            #     new_line = line.split("\n")
            #     for i in range(len(new_line)):
            #         if lines in new_line[i]:
            #             print(new_line[i])
            #         else:
            #             print("没有匹配")
            for line in file:
                if lines in line:
                    print(line.strip())
                    found = True
            if not found:
                print("没找到")
    except FileNotFoundError:
        print("不存在日志文件")


def main():
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write("")
    while True:
        print("\n--- 学习日志管理器 ---")
        print("1. 添加记录")
        print("2. 查看所有记录")
        print("3. 统计记录数量")
        print("4. 搜索关键词")
        print("5. 退出")
        numbers = int(input("输入数字："))
        if numbers == 1:
            add_lines()

        elif numbers == 2:
            read_lines()

        elif numbers == 3:
            count_lines()

        elif numbers == 4:
            lines = input("输入要查找的内容：")
            find_line(lines)

        elif numbers == 5:
            print("退出")
            break
        else:
            print("无效输入")

if __name__ == "__main__":
    main()
