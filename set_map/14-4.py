from collections import Counter

N = input()
cards = Counter(list(map(int, input().split())))
M = input()
nums = list(map(int, input().split()))

for i in nums:
    if i in cards:
        print(cards[i], end=" ")
    else:
        print("0", end=" ")
