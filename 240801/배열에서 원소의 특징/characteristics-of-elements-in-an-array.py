nums = list(map(int, input().split()))

for i, n in enumerate(nums):
    if n % 3 == 0:
        print(nums[i-1])
        break