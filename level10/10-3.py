# 몸무게(x)와 키(y)
# 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때
# x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))
for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
