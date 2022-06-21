from collections import Counter
import sys


input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
nums_dict = Counter(lst)
M = int(input())
answer = list(map(int, input().split()))

for n in answer:
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == n:
            break

        if lst[mid] > n:
            end = mid - 1
        else:
            start = mid + 1

    if lst[mid] == n:
        print(nums_dict[n], end=" ")
    else:
        print(0, end=" ")
