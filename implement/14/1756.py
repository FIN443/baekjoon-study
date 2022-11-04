# 피자굽기
D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

# 더 안쪽에 지름 더 큰거 작은걸로 통일 시킴
for i in range(D - 1):
    if oven[i] < oven[i + 1]:
        oven[i + 1] = oven[i]

cur = 0
for i in range(D - 1, -1, -1):
    if pizza[cur] > oven[i]:
        continue

    cur += 1
    if cur >= N:
        print(i + 1)
        exit()

print(0)
