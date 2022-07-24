# -------- 내 코드 ------------
# nums = list(map(int,input()))
# nums.sort(reverse=True)
#
# for num in nums:
#     print(num, end='')

# ---------- 강의 코드 ----------
array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')