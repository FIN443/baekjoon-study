def solution(m):
    return m % 42


n_list = []
while len(n_list) != 10:
    n = int(input())
    n_list.append(n)
new_list = set(list(map(solution, n_list)))
print(len(new_list))
