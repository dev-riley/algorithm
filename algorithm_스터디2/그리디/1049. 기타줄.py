n, m = map(int, input().split())
p_min, i_min = 1001, 1001
res = 0
for a in range(m):
    p, i = map(int, input().split())
    p_min = min(p_min, p)
    i_min = min(i_min, i)

# 패키지 최소가격이 개별 최소가격은 6개 곱한 것 보다 크면 개별로 6개 사기
if p_min > i_min * 6:
    res += n * i_min
else:
    # 패키지 최소 가격이 더 작다면 n을 6으로 나눈 몫만큼 패키지를 사고
    res += (n // 6) * p_min
    # n을 6으로 나눈 나머지를 개별로 사는게 패키지를 하나 더 사는 것 보다 비싸다면 패키지를 사기
    if (n%6) * i_min > p_min:
        res += p_min
    else:
        # n을 6으로 나눈 나머지를 개별로 사는게 더 싸다면 개별로 나머지 다 사기
        res += (n % 6) * i_min
print(res)
