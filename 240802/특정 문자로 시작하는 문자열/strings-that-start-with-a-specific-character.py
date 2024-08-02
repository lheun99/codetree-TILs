n = int(input())
arr = [input() for i in range(n)]
ch = input()

b = 0
cnt = 0
for a in arr:
    if a[0] == ch:
        cnt += 1
        b += len(a)

print(cnt, "{:.2f}".format(round(b/cnt, 2)))