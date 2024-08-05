a = input()
b = input()

cnt = 1
for i in range(len(a)-1):
    a = a[1:]+a[0]

    if a == b:
        print(cnt)
    cnt += 1

if cnt == len(a):
    print(-1)