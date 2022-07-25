# P일 중, L일동안, V일짜리 휴가 (1 < L < P < V)

count = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    n = V // P
    n2 = L * n
    n3 = V % P
    if L < n3:
        n3 = L

    print(f"Case {count}: {n2 + n3}")
    count += 1
