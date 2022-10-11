# 순열의 순서
import math


N = int(input())
lst = list(map(int, input().split()))
opt = lst.pop(0)


def find_perm_list(n, k):
    if len(answer) == N - 1:
        answer.append(num_list[-1])
        return

    count = math.factorial(n) // n
    seq = math.ceil(k / count)
    answer.append(num_list.pop(seq))

    find_perm_list(n - 1, k - (count * (seq - 1)))


def find_perm_k():
    n = N
    for num in lst:
        count = math.factorial(n) // n
        idx = num_list.index(num)
        if len(num_list) == 2:
            idx += 1
            answer.append(count * idx)
            return
        num_list.pop(idx)
        answer.append(count * idx)
        n -= 1


if opt == 1:
    K = lst[0]
    num_list = [i for i in range(N + 1)]
    answer = []
    find_perm_list(N, K)
    print(" ".join(list(map(str, answer))))

elif opt == 2:
    num_list = [i for i in range(1, N + 1)]
    answer = []
    find_perm_k()
    print(sum(answer))
