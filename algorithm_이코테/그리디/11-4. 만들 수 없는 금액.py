n = int(input())
nums = list(map(int, input().split()))
nums.sort()

target = 1
for x in nums:
    if target < x:
        break
    target += x
print(target)