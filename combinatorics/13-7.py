# 이항계수 nCk -> n! / k!(n-k)!
# 이 함수는 다음 문제에서 런타임 에러 뜸(아마 조건문 때문인듯)
# 그래서 math 내장함수안에 factorial 추천
def factorial(n):
    return n * factorial(n - 1) if n > 0 else 1


n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))


""" 반복문 풀이
a,b = map(int, input().split())
ans = 1
for i in range(b) :
    ans = ans*(a-i)
for j in range(b) :
    ans = int(ans/(j+1))
print(ans)
"""
