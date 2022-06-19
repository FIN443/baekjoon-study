N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))


def multi(m1, m2):
    m3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                m3[i][j] += m1[i][k] * m2[k][j]

    for i in range(N):
        for j in range(N):
            m3[i][j] %= 1000
    return m3


def solution(a, b):
    if b == 1:
        return a

    func = solution(a, b // 2)

    if b % 2 == 0:
        return multi(func, func)
    else:
        return multi(multi(func, func), a)


result = solution(A, B)
for row in result:
    for num in row:
        print(num % 1000, end=" ")
    print()
