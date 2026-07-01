#test10
from datetime import datetime, date, timedelta

# # 当前日期和时间
# now = datetime.now()
# print(now)  # 2026-07-01 14:30:25.123456
# 当前日期（只有年月日）
today = date.today()
data_str = input("输入日期（格式YYYY-MM-DD）：")
dt = datetime.strptime(data_str, "%Y-%m-%d").date()
delta = today - dt
age = delta.days // 365
print(age)