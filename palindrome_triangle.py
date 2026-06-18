#Palindrome Traingle

n = 5

for i in range(n):
    for k in range(n - i - 1):
        print(" ",end ="")

    for j in range(i+1,1,-1):
        print(j,end = "")

    for l in range(i+1):
        print(l + 1,end = "")

    print()