#Arrow Pattern
n = 5

for i in range(n):
    spaces = n // 2 + 2
    stars = n // 2 + 1
    print(spaces * " " + stars * "*")

for i in range(n):
    spaces = i + 1
    stars = 2 * (n - i) - 1
    print(spaces * " " + stars * "*")

