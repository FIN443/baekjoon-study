from collections import deque


N, M = map(int, input().split())
if N == 0:
    print(0)
    exit()
books = list(map(int, input().split()))
que = deque(books)

left = M
count = 0
while que:
    book = que.popleft()
    left -= book
    if book > M:
        break
    elif not que and left >= 0:
        count += 1
        break
    elif left > 0:
        continue
    elif left < 0:
        que.appendleft(book)
    left = M
    count += 1


print(count)


"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
if N == 0:
    print(0)
    exit()
lst = list(map(int,input().split()))
cnt = 0
nums = 0

for i in lst:
    if nums + i <= M:
        nums = nums + i
    else:
        cnt += 1
        nums = i

print(cnt+1)
"""
