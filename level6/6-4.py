def solution(m):
    return m * count


n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input().split())

for row in n_list:
    word = row.pop()
    count = int(row.pop())
    word = list(map(solution, word))
    print(*word, sep="")
