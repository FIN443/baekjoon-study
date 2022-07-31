N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

result = max(lst, key=lambda x: x[0])[0] - min(lst, key=lambda x: x[1])[1]

if result < 0:
    print(0)
else:
    print(result)
