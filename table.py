n = 10
for i in range(1, n + 1):
    for j in range(1, n + 1):
        square = i * j
        print(f"{square:5}", end="")
    print()