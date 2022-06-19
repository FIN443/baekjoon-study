A, B, C = map(int, input().split())


def solution(a, b):
    if b == 1:
        return a % C

    # 요거 안하니까 시간초과
    func = solution(a, b // 2)

    if b % 2 == 0:
        return (func * func) % C
    else:
        return (func * func * a) % C


print(solution(A, B))


""" 분배법칙
a = 10 , b = 11 , c = 12
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
"""
