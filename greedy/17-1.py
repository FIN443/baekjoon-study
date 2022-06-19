N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
cost = lst.pop()
result = 0
while K > 0:
    if K < cost:
        cost = lst.pop()
        continue
    result += K // cost
    K = K % cost
print(result)
