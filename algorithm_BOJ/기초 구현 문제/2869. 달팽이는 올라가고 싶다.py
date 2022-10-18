#-----시간초과---------------
a, b, v = map(int, input().split())
# ans = 0
# day = 0
# while v > ans:
#     day += 1
#     ans += a
#     if ans >= v:
#         break
#     ans -= b
#
# print(day)
#-----------------------------------------------
# (v-a) : 낮맞에 도달, (a-b): 하루동안 갈 수 있는 거리
ans = (v-a) // (a-b)
if (v-a) % (a-b) == 0:
    print(ans + 1)
else:
    print(ans + 2)