# A와 B 2
S = input()
T = input()


def dfs(T):
    if T == S:
        print(1)
        exit()

    if len(T) == 0:
        return

    if T[-1] == "A":
        dfs(T[:-1])

    if T[0] == "B":
        dfs(T[1:][::-1])


dfs(T)
print(0)
