N, L = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort()

for i in fruit:
    if i <= L:
        L += 1
print(L)
