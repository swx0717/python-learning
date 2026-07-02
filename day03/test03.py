number = int(input("Enter a number: "))
for i in range(1, 10):
    for j in range(1, i+1):
        if number == j or number == i:
            print(f"{j}×{i}={i*j}")