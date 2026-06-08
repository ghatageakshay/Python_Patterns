#Hardcoded
# n = 4
# for i in range(n):
#     for j in range(i+1):
        
#         if j == 0 or j == i:
#             print("1",end="")

#         elif (i == 2 and j == 1):
#             print("2",end = "")

#         elif(i == 3 and (j ==1 or j == 2)):
#             print("3",end = "")
#     print()

#dynamic
import math

n = 5
for i in range(n):

    for k in range(n-i-1):
        print(" ",end = "")
    for j in range(i+1):

        print(math.comb(i,j),end = "")

    print()