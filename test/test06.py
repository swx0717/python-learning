import json
# #
# # 通讯录管理器
# # def load_contacts():
# #     # 中文逻辑 1：尝试打开文件 contacts.json 读取
# #     # 中文逻辑 2：如果文件不存在 或 JSON 损坏，返回空列表 []
# #     # 提示：用 try...except...
# #     # 你的代码写在这里 ↓
# #     try:
# #         with open("contacts.json", "r",encoding="=utf-8") as f:
# #             return json.load(f)
# #     except (FileNotFoundError, json.decoder.JSONDecodeError):
# #         return []
# #
# # def save_contacts(contacts):
# #     # 中文逻辑 1：用 'w' 模式打开文件
# #     # 中文逻辑 2：json.dump 写入，缩进 2，支持中文
# #     # 你的代码写在这里 ↓
# #     with open("contacts.json", "w", encoding="utf-8") as f:
# #         json.dump(contacts, f, ensure_ascii=False, indent=2)
# #
# # def add_contact(contacts, name, phone):
# #     # 中文逻辑 1：把 {"name": name, "phone": phone} 追加到 contacts 列表
# #     # 中文逻辑 2：调用 save_contacts(contacts) 保存
# #     # 你的代码写在这里 ↓
# #     with open("contacts.json", "a", encoding="utf-8") as f:
# #         contacts.append({"name": name, "phone": phone})
# #         save_contacts(contacts)
# #
# # def delete_contact(contacts, name):
# #     # 中文逻辑 1：遍历 contacts 列表，找到 name 匹配的项
# #     # 中文逻辑 2：如果找到了，从列表中移除它（用 remove 或 pop）
# #     # 中文逻辑 3：调用 save_contacts(contacts) 保存，打印“删除成功”
# #     # 中文逻辑 4：如果遍历完都没找到，打印“未找到该联系人”
# #     # 你的代码写在这里 ↓
# #     found = False
# #     for contact in contacts:
# #         if contact["name"] == name:
# #             contacts.remove(contact)  # 或 contacts.pop(index)
# #             save_contacts(contacts)
# #             print(f"联系人 {name} 已删除")
# #             found = True
# #             break
# #     if not found:
# #         print(f"未找到联系人：{name}")
# #
# #
# # def main():
# #     contacts = load_contacts()
# #     while True:
# #         print("\n1. 添加联系人")
# #         print("2. 删除联系人")
# #         print("3. 退出")
# #         choice = input("请选择：")
# #         if choice == "1":
# #             name = input("姓名：")
# #             phone = input("联系号码：")
# #             add_contact(contacts, name, phone)
# #         elif choice == "2":
# #             name = input("输入要删除的联系人姓名：")
# #             delete_contact(contacts, name)
# #         elif choice == "3":
# #             break
# #         else:
# #             print("无效输入")
# #
# # if __name__ == "__main__":
# #     main()
#
# 游戏高分榜
# def load_scores():
#     try:
#         with open("scores.json", "r", encoding="utf-8") as f:
#             return json.load(f)
#     except(FileNotFoundError, json.JSONDecodeError):
#             return[]
#
# def save_scores(scores):
#     with open("scores.json", "w", encoding="utf-8") as f:
#         json.dump(scores, f, ensure_ascii=False,indent=2)
#
# def add_score(scores, player, score):
#     # 中文逻辑 1：将新玩家字典追加到 scores 列表
#     # 中文逻辑 2：保存
#     scores.append({"player":player,"score":score})
#     save_scores(scores)
#
# def get_top_three(scores):
#     # 中文逻辑 1：对 scores 列表按 "score" 字段倒序排序（降序）
#     # 中文逻辑 2：返回排序后列表的前 3 个元素（切片）
#     # 提示：排完序后 new_list = sorted(...) ; return new_list[:3]
#     data_sorted = sorted(scores, key=lambda x: x["score"], reverse=True)
#     scores = data_sorted[:3]
#     return scores
#
#     pass
#
# # 测试代码（写到 main 里）
# def main():
#     scores = load_scores() # 假设你写好了加载函数
#     # 手动加几条数据测试
#     add_score(scores, "Alice", 100)
#     add_score(scores, "Bob", 300)
#     add_score(scores, "Charlie", 200)
#     add_score(scores, "David", 150)
#     print(get_top_three(scores))  # 应该输出 Bob, Charlie, Alice
#
# if __name__ == "__main__":
#     main()

# 购物车小工具
def load_cart():
    try:
        with open("cart.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save_cart(cart):
    with open('cart.json', 'w') as f:
        json.dump(cart, f, ensure_ascii=False, indent=2)

def update_qty(cart, item_name, new_qty):
    # 中文逻辑 1：遍历 cart 列表，找 item 等于 item_name 的项
    # 中文逻辑 2：如果找到了：
    #   如果 new_qty <= 0: 从列表中 remove 该元素（删除）
    #   否则：将该元素的 "qty" 修改为 new_qty
    # 中文逻辑 3：如果没找到，打印“商品不存在”
    # 中文逻辑 4：无论如何（只要修改了），调用 save_cart(cart)
    found = False
    for item in cart:
        if item["item_name"] == item_name:
            if new_qty <= 0 :
                cart.remove(item)
                save_cart(cart)
                print("已经删除")
            else:
                item["qty"] = new_qty
                save_cart(cart)
                print("更新成功")
            found = True
            break
    if not found:
        print("没找到该商品")


def calc_total(cart):
    # 中文逻辑 1：定义一个变量 total = 0.0
    # 中文逻辑 2：遍历列表，把每个 item["price"] * item["qty"] 累加到 total
    # 中文逻辑 3：返回 total
    total = 0.0
    for item in cart:
        total += item["qty"]*item["price"]
    print(total)

def main():
    cart = load_cart()
    # 手动添加一些商品（方便测试）
    if not cart:
        cart = [
            {"item_name": "苹果", "price": 5.5, "qty": 3},
            {"item_name": "香蕉", "price": 3.0, "qty": 2}
        ]
        save_cart(cart)

    print("当前购物车：", cart)
    print("总价：", calc_total(cart))

    # 测试修改数量
    update_qty(cart, "苹果", 5)        # 改为5
    update_qty(cart, "香蕉", 0)        # 删除
    update_qty(cart, "橙子", 1)        # 不存在

    print("最终购物车：", cart)
    print("总价：", calc_total(cart))

if __name__ == "__main__":
    main()
