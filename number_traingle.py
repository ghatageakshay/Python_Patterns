#Number_triangle Pattern
n = 4

for i in range(n):

    for k in range(n -i -1):
        print(" ",end ="")

    for j in range(1,i + 2):
        print(j,end = "")

    for l in range(i,0,-1):
        print(l,end = "")

    print()