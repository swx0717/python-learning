number = int(input("Enter a number: "))
if number < 2:
    print("不是")
else:
    is_prime = True
    for i in range(2, number):
        if number % 2 == 0:
            is_prime = False
            break
    if is_prime:
        print("是")
    else:
        print("不是")