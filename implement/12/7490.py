# 0 만들기
T = int(input())


def solution(lst, n):
    if len(lst) == n:
        operations.append(lst[:])
        return

    lst.append(" ")
    solution(lst, n)
    lst.pop()

    lst.append("+")
    solution(lst, n)
    lst.pop()

    lst.append("-")
    solution(lst, n)
    lst.pop()


for _ in range(T):
    N = int(input())
    operations = []
    solution([], N - 1)

    for oper in operations:
        line = ""
        for i in range(N - 1):
            line += str(i + 1) + oper[i]

        line += str(N)
        if (eval(line.replace(" ", ""))) == 0:
            print(line)

    print()
