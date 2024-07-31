n = int(input())

for i in range(n):
    print("* ", end="")
print()
for i in range(1, n):
    print("* " * i, end="")
    print("  " * (n-(i+1)), end="")
    print("*")