n, m = map(int,input().split())
# n개의 화폐 단위 정보받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# DP 진행(보텀업)
d[0] = 0
for i in range(n): # i는 각각의 화폐단위
    for j in range(array[i], m + 1): # j는 각각의 금액
        if d[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
