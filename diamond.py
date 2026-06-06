n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    
    print("*",end="")

    for m in range(2*i-1):
        print(" ",end="")

    if i!=0:

        print("*",end="")


    print()

for i in range(1,n):
    for j in range(i):
        print(" ",end="")

    print("*",end="")

    for k in range(2*(n-i)-3):
        print(" ",end="")

    if i!=n-1:
        print("*",end="")

    print()