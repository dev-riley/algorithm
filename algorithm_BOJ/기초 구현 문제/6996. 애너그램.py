for tc in range(int(input())):
    A, B = input().split()
    A1 = ''.join(sorted(A))
    B1 = ''.join(sorted(B))
    if A1 == B1:
        print('%s & %s are anagrams.' % (A, B))
    else:
        print('%s & %s are NOT anagrams.' % (A, B))