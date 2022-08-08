# 등수 매기기
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

result = 0
for i in range(1, N + 1):
    result += abs(i - lst[i - 1])
print(result)

""" 이게 왜 됨...?
1 1 2 3 5
1 2 3 4 5
"""
