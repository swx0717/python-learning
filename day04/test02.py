str = "hello world"
counts = []
seen = []
for char in str:
    if char in seen:
        index = seen.index(char)
        counts[index] += 1
    elif char not in seen:
        seen.append(char)
        counts.append(1)
count_dict = dict(zip(seen,counts))
print(count_dict)