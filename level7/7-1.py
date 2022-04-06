import math


a = 1000  # 고정비용
b = 70  # 변동비용
c = 170  # 측정비용

# a + b*n > c*n 일 때 손익 발생

a, b, c = map(int, input().split())
if c - b > 0:
    print(math.floor(a / (c - b)) + 1)
else:
    print(-1)
