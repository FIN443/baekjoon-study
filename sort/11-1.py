T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))
print(*sorted(lst), sep="\n")
