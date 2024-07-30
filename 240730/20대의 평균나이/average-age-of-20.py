res = 0
cnt = 0
while True:
    n = int(input())

    if n > 29:
        break
    else:
        res += n
        cnt += 1
    
print("{:.2f}".format(res/cnt))