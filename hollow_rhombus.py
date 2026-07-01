#Hollow Rhombus Pattern
n = 5

for i in range(n):
    for k in range(n - i - 1):
        print(" ",end = " ")

    for j in range(n):
        if j == 0 or j == n - 1 or i == 0 or i == n - 1:
            print("*" , end = " ")

        else:
            print(" ",end = " ")

    print()
