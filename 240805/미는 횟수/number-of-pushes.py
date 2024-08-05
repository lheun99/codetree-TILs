a = input()
b = input()

cnt = 1
for i in range(len(a)-1):
    a = a[-1]+a[0:-1]

    if a == b:
        print(cnt)
        break
    cnt += 1

if cnt == len(b):
    print(-1)