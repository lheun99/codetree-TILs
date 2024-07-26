nums = list(map(int, input().split()))

print(sum(nums))
print(sum(nums)//len(nums))
print(sum(nums) - sum(nums)//len(nums))