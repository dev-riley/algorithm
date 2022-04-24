import sys
from collections import Counter
n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

# 산술평균
sum = 0
for num in nums:
    sum += num
avg = round(sum /n)

# 중앙값
mid = round(nums[n//2])

# 최빈값
cnt = Counter(nums).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    max_cnt = cnt[1][0]
else:
    max_cnt = cnt[0][0]

# 범위
rng = nums[-1] - nums[0]

print(avg)
print(mid)
print(max_cnt)
print(rng)