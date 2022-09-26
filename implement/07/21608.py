# 상어 초등학교
N = int(input())
students = []
for _ in range(N**2):
    students.append(list(map(int, input().split())))

table = [[0 for _ in range(N)] for _ in range(N)]

for order in range(N**2):
    student = students[order]
    done = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                like_n = 0
                blank_n = 0
                for dx, dy in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= dx < N and 0 <= dy < N:
                        if table[dx][dy] in student[1:]:
                            like_n += 1
                        if table[dx][dy] == 0:
                            blank_n += 1
                done.append([like_n, blank_n, i, j])
    done.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    table[done[0][2]][done[0][3]] = student[0]

result = 0
students.sort()

for i in range(N):
    for j in range(N):
        ans = 0
        for dx, dy in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            if 0 <= dx < N and 0 <= dy < N:
                if table[dx][dy] in students[table[i][j] - 1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans - 1)

print(result)
