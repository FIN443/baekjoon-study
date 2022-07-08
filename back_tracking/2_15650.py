N, M = map(int, input().split())

lst = []


def dfs(lst):
    if len(lst) == M:
        for i, j in zip(lst, lst[1:]):
            if i > j:
                return
        print(*lst, sep=" ")
        return

    for i in range(1, N + 1):
        if i not in lst:
            lst.append(i)
            dfs(lst)
            lst.pop()


dfs(lst)
