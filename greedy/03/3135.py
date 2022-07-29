start, end = map(int, input().split())
N = int(input())
save = []
for _ in range(N):
    k = int(input())
    save.append(k)

result = [abs(start - end) - 1]
for i in save:
    result.append(abs(i - end))


print(min(result) + 1)
