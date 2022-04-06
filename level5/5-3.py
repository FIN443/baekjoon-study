def solution(m):
    if m < 10:
        return 1
    if m < 100:
        return 1
    if i < 1000:
        m_str = str(m)
        m_list = list(map(int, m_str))
        a = m_list.pop()
        b = m_list.pop()
        c = m_list.pop()
        if a - b == b - c:
            return 1
    return 0


n = int(input())
result = 0
for i in range(1, n + 1):
    result += solution(i)
print(result)
