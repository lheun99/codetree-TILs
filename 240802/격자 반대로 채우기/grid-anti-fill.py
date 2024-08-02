n = int(input())
nums = [[] for i in range(n)]

cnt = 0
for i in range(1, pow(n, 2)+1):
    for j in range(n):
        nums[j].append(i)
        cnt += 1

        if cnt 

print(nums)