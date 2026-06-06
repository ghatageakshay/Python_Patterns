n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")

    for k in range(2*(n-i-1)):
        print(" ",end="")

    for m in range(i+1):
        print("*",end="")

    print()

for l in range(n):
    for x in range((n-l-1)):
        print("*",end="")

    for y in range(2*l+2):
        print(" ",end="")

    for z in range(n-l-1):
        print("*",end="")

    print()