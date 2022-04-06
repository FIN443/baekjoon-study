import math


def solution(m):
    if m < 10:
        return m + math.floor(m / 1)
    if m < 100:
        return m + math.floor(m / 10) + m % 10
    if m < 1000:
        return m + math.floor(m / 100) + math.floor(m / 10) % 10 + m % 10
    if m < 10000:
        m = m + math.floor(m / 1000) + math.floor(m / 100) % 10 + math.floor(m / 10) % 10 + m % 10
        return m if m < 10000 else 0


n_list = set(range(0, 10000))
m_list = set()
for i in range(1, 9999):
    m_list.add(solution(i))
result = sorted(n_list - m_list)
for i in result:
    print(i)
