#ButerrFly Pattern

n = 5
for i in range(n):
    stars = i + 1
    spaces = 2 * (n - stars)

    print("*" * stars + " " * spaces + "*" * stars)

for i in range(n):
    stars = n - i - 1
    spaces = 2 * i + 2
    print("*" * stars + " " * spaces + "*" * stars)