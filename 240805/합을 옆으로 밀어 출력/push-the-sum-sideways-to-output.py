n = int(input())

num = 0
for i in range(n):
    num += int(input())

print(str(num)[1:] + str(num)[0])