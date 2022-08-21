# 수강신청
import sys


input = sys.stdin.readline
K, L = map(int, input().split())
waiting = []
check = {}
for i in range(L):
    std = input().rstrip()
    try:
        if check[std]:
            del check[std]
    except:
        pass
    check[std] = 1

count = 0
for i in check.keys():
    if count >= K:
        break
    print(i)
    count += 1


"""
import sys


input = sys.stdin.readline
K, L = map(int, input().split())
waiting = {}
for i in range(L):
    std = input().rstrip()
    waiting[std] = i

new_lst = list(waiting.items())
new_lst.sort(key=lambda x: x[1])

count = 0
for k, v in new_lst:
    if count >= K:
        break
    print(k)
    count += 1
"""
