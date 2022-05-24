N, M = map(int, input().split())
no_listen = set([input() for _ in range(N)])
no_seen = set([input() for _ in range(M)])

result = list(no_listen.intersection(no_seen))
result.sort()

print(len(result))
print(*result, sep="\n")
