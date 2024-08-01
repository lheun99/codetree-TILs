n = int(input())

nums = list(map(int, input().split()))

for i in range(n, 0, -1):
    if nums[i-1] % 2 == 0:
        print(nums[i-1], end = " ")