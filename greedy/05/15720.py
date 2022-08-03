from collections import deque


B, C, D = map(int, input().split())

bugger = deque(sorted(list(map(int, input().split())), reverse=True))
side = deque(sorted(list(map(int, input().split())), reverse=True))
drink = deque(sorted(list(map(int, input().split())), reverse=True))

result = 0
result_sale = 0
while bugger and side and drink:
    a = bugger.popleft()
    b = side.popleft()
    c = drink.popleft()
    result += a + b + c
    result_sale += int((a + b + c) * 0.9)

result += sum(bugger) + sum(side) + sum(drink)
result_sale += sum(bugger) + sum(side) + sum(drink)

print(result, result_sale, sep="\n")
