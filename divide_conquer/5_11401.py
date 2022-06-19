N, K = map(int, input().split())
p = 1000000007


def factorial(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % p
    return n


def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p


# nCk = n! / (n-k)!k!
top = factorial(N)
bottom = factorial(N - K) * factorial(K) % p

# 페르마의 소정리
print(top * square(bottom, p - 2) % p)

""" 분배법칙
(A + B) % p = ((A % p) + (B % p)) % p
(A x B) % p = ((A % p) x (B % p)) % p
(A - B) % p = ((A % p) - (B % p) + p) % p
"""

# 카르마의 소법칙
# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11401-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-3-%EA%B3%A8%EB%93%9C1-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
