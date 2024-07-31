n = int(input())

print("*")
for i in range(1, n):
    if n % 2 == 0:
        a = i * 2
    else:
        a = i * 2 + 1

    print("*" * a)