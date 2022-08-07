# 블랙잭
N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

result = 0
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if cards[i] + cards[j] + cards[k] <= M:
                result = max(result, cards[i] + cards[j] + cards[k])

print(result)
