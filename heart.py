#Heart Pattern

n = 5
for i in range(2):
    for j in range(2*n):
        if (i == 0 and(j == 0 or j == n-1 or j == n or j == 2*n - 1)) or (
            i == 1 and(j == n-1 or j == n)
        ):
            print(" ", end = " ")

        else:
            print("*", end = " ")

    print()

for i in range(n):
    for k in range(i + 1):
        print(" " , end = " ")

    for j in range(2 * (n - i) - 1):
        print("*" , end = " ")

    print()