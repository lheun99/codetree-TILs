a, b = map(int, input().split())

res = 1
for i in range(a, b+1):
    if i%a == 0:
        res *= i

print(res)