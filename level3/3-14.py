import math


n = int(input())
result = n
count = 0

while True:
    front = math.floor(result / 10)
    back = result % 10
    result = back * 10 + (front + back) % 10
    count += 1
    if result == n:
        break
print(count)
