arr = []

for i in range(10):
    N = int(input())
    arr.append(N % 42)
arr = set(arr) # set : 중복 값 제거
print(len(arr))

#----------------------------------
# 2번째 방법
# arr = []
# for _ in range(10):
#     m = int(input()) % 42
#     if m not in arr:
#         arr.append(m)
# print(len(arr))