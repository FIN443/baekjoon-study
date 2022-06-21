import sys


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
stack = [0]


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if stack[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return start


for i in A:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[(binary_search(0, len(stack) - 1, i))] = i

print(len(stack) - 1)
