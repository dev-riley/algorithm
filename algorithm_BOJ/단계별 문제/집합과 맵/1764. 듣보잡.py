import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr_n = [input().rstrip() for i in range(n)]
arr_m = [input().rstrip() for i in range(m)]

# set은 집합으로 합집합(|), 교집합(&), 차집합(-) 등을 사용할 수 있다.
d = list(set(arr_n) & set(arr_m))

print(len(d))
for i in sorted(d):
    print(i)