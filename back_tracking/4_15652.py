N, M = map(int, input().split())

lst = []


def dfs(lst):
    if len(lst) == M:
        print(*lst, sep=" ")
        return

    for i in range(1, N + 1):
        if not lst:
            lst.append(i)
            dfs(lst)
            lst.pop()
        elif lst and lst[-1] <= i:
            lst.append(i)
            dfs(lst)
            lst.pop()


dfs(lst)
