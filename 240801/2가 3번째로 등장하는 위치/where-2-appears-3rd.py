n = int(input())
nums = list(map(int, input().split()))

cnt = 3
for i, j in enumerate(nums):
    if j == 2:
        cnt -= 1

        if cnt == 0:
            print(i+1)