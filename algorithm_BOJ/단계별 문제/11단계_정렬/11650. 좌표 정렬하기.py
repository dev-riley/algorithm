import sys
# n = int(input())
#
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#
# arr.sort()
# for a in arr:
#     for b in a:
#         print(b, end=" ")
#     print()

# ------------------------------------------------------
n = int(input())
arr = []
for i in range(0, n):
    arr.append(sys.stdin.readline())

arr.sort(key=lambda x: (int(x.split()[0]), int(x.split()[1])))
print(" ".join(arr))
