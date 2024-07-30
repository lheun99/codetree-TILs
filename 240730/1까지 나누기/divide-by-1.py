a = int(input())

res = 1
for i in range(1, a+1):
    if a // i <= 1:
        break
    else:
        a //= i
        res += 1

print(res)