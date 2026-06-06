#hollow square
n=5
mid=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-3 or i==0:
            print(" *",end="")

        else:
            print("  ",end="")
    for s in range(n-2):
        print(" ",end="")

        
    for k in range(n):
        if k==0 or i + k == mid or i - k == mid  :
            print("  *",end="")

        elif(k==1 and i==mid):
            print(" *",end="")

        else:
            print(" ",end="")

    for s in range(n-2):
        print(" ",end="")

    for x in range(n):
        if i==0 or i==n-1 :
            print("* ",end="")

        
        elif i==mid:
            print(" *",end="")

        elif(x==0 and i==1):
            print("*",end="")

        elif (x==n-1 and i==n-2):
            print("    *",end="")

        # elif(x==0 and i<=n-2):
        #     print(" *",end="")
        else:
            print(" ",end="")

    for l in range(n-2):
        print("  ",end="")

    for h in range(n):
        if h==0 or h==n-1 or i==mid:
            print(" *",end="")

        else:
            print(" ",end="")

    
    print()

