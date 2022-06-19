N = int(input())
check_lst = list(map(int, input().split()))
M = int(input())
input_lst = list(map(int, input().split()))


def binary_search(target, lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid + 1  # 0번째를 return 하면 아래 if idx에서 0은 else로 필터된다
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


sorted_lst = sorted(check_lst)
for n in input_lst:
    idx = binary_search(n, sorted_lst)
    if idx:
        print(1)
    else:
        print(0)

""" 이분탐색
# lst는 정렬되있어야 함
def binary_search(target, lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid + 1  # 0번째를 return 하면 아래 if idx에서 0은 else로 필터된다
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


sorted_lst = sorted(check_lst)
for n in input_lst:
    idx = binary_search(n, sorted_lst)
    if idx:
        print(1)
    else:
        print(0)
"""

""" 집합
N = int(input())
check_lst = set(map(int, input().split()))
M = int(input())
input_lst = list(map(int, input().split()))

for i in input_lst:
    if i in check_lst:
        print(1)
    else:
        print(0)
"""

""" 해시
from collections import Counter


N = int(input())
check_lst = Counter(map(int, input().split()))
M = int(input())
input_lst = list(map(int, input().split()))

for i in input_lst:
    if check_lst[i]:
        print(1)
    else:
        print(0)
"""
