N = 2
A = [[1, 1], [1, 0]]
B = int(input())


def multi(m1, m2):
    m3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                m3[i][j] += m1[i][k] * m2[k][j]

    for i in range(N):
        for j in range(N):
            m3[i][j] %= 1000000007
    return m3


def solution(a, b):
    if b == 1:
        return a

    func = solution(a, b // 2)

    if b % 2 == 0:
        return multi(func, func)
    else:
        return multi(multi(func, func), a)


print(solution(A, B)[0][1] % 1000000007)
