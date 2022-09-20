# 빗물
H, W = map(int, input().split())
table = list(map(int, input().split()))
stack = []

left = 0
right = 0
result = 0
for i in range(1, W - 1):
    left = max(table[:i])
    right = max(table[i + 1 :])

    bound = min(left, right)

    if table[i] < bound:
        result += bound - table[i]

print(result)
