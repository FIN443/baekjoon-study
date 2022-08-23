# 추월
import sys


input = sys.stdin.readline
N = int(input())
car_in = {}
car_out = []
for i in range(N):
    v = input().rstrip()
    car_in[v] = i


for i in range(N):
    v = input().rstrip()
    car_out.append(v)

count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        a = car_in[car_out[i]]
        b = car_in[car_out[j]]
        if a > b:
            count += 1
            break

print(count)


"""
a b c d
d a c b
"""

"""
import sys


input = sys.stdin.readline
N = int(input())
car_out = {}
lst = []
for i in range(N):
    v = input().rstrip()
    lst.append(v)

for i in range(N):
    v = input().rstrip()
    car_out[v] = i

count = 0
for front, back in zip(lst, lst[1:]):
    a = car_out[front]
    b = car_out[back]
    if a > b:
        count += 1

print(count)
"""
