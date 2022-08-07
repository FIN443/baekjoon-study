def check(x):
    for i in range(x):
        if (table[x] == table[i]) or (abs(table[x] - table[i]) == x - i):
            return False
    return True


def dfs(n):
    global count
    if n == N:
        count += 1
    else:
        for i in range(N):
            if visited[i]:
                continue

            table[n] = i
            if check(n):
                visited[i] = True
                dfs(n + 1)
                visited[i] = False


N = int(input())
table = [0 for _ in range(N)]
visited = [False for _ in range(N)]
count = 0
dfs(0)
print(count)
