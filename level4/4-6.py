def solution(m):
    m_list = []
    count = 0
    for i in range(0, len(m)):
        if m[i] == "O":
            count += 1
            m_list.append(count)
        else:
            count = 0
            m_list.append(count)
    print(sum(m_list))
    return sum(m_list)


n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input())
result = list(map(solution, n_list))
