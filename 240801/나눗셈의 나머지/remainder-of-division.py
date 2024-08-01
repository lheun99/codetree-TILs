from collections import Counter
a, b = map(int, input().split())

nums = []

while a > 1:
    nums.append(a % b)
    a = a // b

dicts = Counter(nums)

res = 0
for i, j in dicts.items():
    res += pow(j, 2)

print(res)