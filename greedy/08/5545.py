N = int(input())
A, B = map(int, input().split())
C = int(input())
D = []
for _ in range(N):
    D.append(int(input()))
D.sort(reverse=True)

price = A
kcal = C
for i in range(N):
    if (kcal + D[i]) / (price + B) > kcal / price:
        kcal += D[i]
        price += B
    else:
        break

print(int(kcal / price))
