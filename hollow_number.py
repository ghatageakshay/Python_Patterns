n = 5

for i in range(n):
    for k in range(n - i - 1):
        print(" ", end="")

    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:  
            print(i, end=" ")
        else:
            print(" ", end=" ")

    print()