odd_sum = 0
for number in range(1,101):
    if number % 2 == 0:
        print(number)
    if number % 2 != 0:
        odd_sum += number
print(odd_sum)