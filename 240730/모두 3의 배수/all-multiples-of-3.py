res = 1
for i in range(5):
    a = int(input())

    if a % 3 != 0:
       res = 0
       break

print(res)