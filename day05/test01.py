# def greet(name):
#     """"返回问候语"""
#     return "hello, " + name
# message = greet("小明")
# print(message)
#
# def power(base, exponent):
#     return base ** exponent
# print(power(2,3))
#
# def power_default(base, exponent=2):
#     return base ** exponent
# print(power_default(3))
# print(power_default(3,4))
#
# def change_local():
#     x = 10
#     print("函数内部x = ",x)
#     x = 5
#     change_local()
#     print("全局 x=",x)

# def add_numbers(a :int,b :int) -> int:
#     return a+b
# result = add_numbers(10,2)
# add_numbers("3","4")
# print(result)
# print(add_numbers("3", "4"))

def get_scores():
     return [float(x) for x in input("输入分数（用空格分隔）：").strip().split()]

def calc_average(scores):
     return sum(scores)/len(scores)

def display(avg):
     print(f"平均分：{avg}")

def main():
    print("程序开始")
    scores = get_scores()
    avg = calc_average(scores)
    display(avg)

if __name__ == "__main__":
    main()

# def bad_process():
#     """（演示错误）不要使用这个函数，它会导致 TypeError"""
#     scores = input("输入分数：")
#     # 下面这行会报错，因为 sum 不能直接作用于字符串
#     # avg = sum(scores) / len(scores)
#     # print(avg)

def get_scores():
    """从用户输入获取分数列表，输入为空时返回空列表"""
    raw = input("输入分数（用空格分隔）：").strip()
    if not raw:          # 如果用户直接回车
        return []
    return [float(x) for x in raw.split()]

def calc_average(scores):
    """计算平均值，空列表返回 0.0"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def display(avg):
    """显示平均分"""
    print(f"平均分：{avg:.2f}")

def main():
    """主程序：获取分数、计算、显示"""
    scores = get_scores()
    avg = calc_average(scores)
    display(avg)

# 调用主函数（只有直接运行此脚本时才执行）
if __name__ == "__main__":
    main()