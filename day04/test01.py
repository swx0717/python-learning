# str = [1,2,5,4]
# str_1=list(reversed(str))
# print(str_1)
# print(str)

text = "hello students"
unique = []
repeated = []
for char in text:
    if text.count(char) == 1:
        unique.append(char)
    elif char not in repeated:
        repeated.append(char)
print("没有重复：", unique)
print("出现重复：", repeated)

counts = {}

for char in text:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
print(counts)