# import string
#
# sentence = input("输入英文文本（单词用空格间隔）：")
#
# clean_char = []
# for char in sentence:
#     if char not in string.punctuation:
#         clean_char.append(char)
# sentence = "".join(clean_char)
# sentence = sentence.lower()
# sentence = sentence.split()
# print(sentence)
# # seen = []
# # counts = []
# # for word in sentence:
# #     if word in seen:
# #         index = seen.index(word)
# #         counts[index] +=1
# #     else:
# #         seen.append(word)
# #         counts.append(1)
# counts = {}
# for word in sentence:
#     counts[word] = counts.get(word,0)+1
# print(counts)
#
# # def get_counts(item):
# #     return item[1]
# # sorted_counts = sorted(counts.item(),key = get_counts ,reverse = True)
# # print(sorted_counts)
# sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
# print(sorted_items)
# max_word = sorted_items[0][0]
# max_count = sorted_items[0][1]
# print(f"次数最多的单词：{max_word}，次数：{max_count}")
# scores = [90, 78, 90, 65, 78, 90, 82, 65, 65, 78, 90, 70]
#
# # ----- 第一步：统计词频（这里用字典） -----
# freq = {}
# for score in scores:
#     # 请填空：如果字典里没有这个分数，就设为1；如果有，就加1
#     # 提示：用 freq.get(score, 0)
#     freq[score] = freq.get(score, 0) + 1
#
# # ----- 第二步：按出现次数排序（找出最高频） -----
# # 请将 freq 里的键值对，按 值（次数） 进行降序排序
# sorted_items = sorted(freq.items(), key=lambda item: item[0], reverse=True)
#
# # 最高频的分数和次数
# max_score = sorted_items[0][0]   # 取分数
# max_count = sorted_items[0][1]   # 取次数
# print(f"最高频分数：{max_score}，出现 {max_count} 次")
#
# # ----- 第三步：按分数（键）升序输出 -----
# # 对 freq 里的键值对，按 键（分数） 进行升序排序
# sorted_by_score = sorted(freq.items(), key=lambda item: item[1])  # 注意这里不写 reverse
# print("\n按分数升序统计：")
# for score, count in sorted_by_score:
#     print(f"{score}分: {count} 次")
#
dict_1 ={"张三":"18642215775"}
while True:
    print("通讯录")
    print("按1：添加\n按2：查询\n按3：删除\n按4：退出")
    switch = input("选择功能（填写数字如：1）：")
    if switch == "1":
        name = input("输入姓名:")
        number = input("输入号码:")
        if len(number) != 11:
            print("输入正确的号码")
        else:
            dict_1.update({name:number})
            print(dict_1)
    elif switch == "2":
        name = input("输入查询的联系人：")
        if name in dict_1:
            print(f"查询号码为{dict_1[name]}")
        else:
            print("不存在该联系人")
    elif switch == "3":
        name = input("输入要删除的联系人：")
        if name in dict_1:
            del dict_1[name]
            print(dict_1)
        else:
            print("不存在该联系人")
    elif switch == "4":
        print("感谢使用，再见")
        break

