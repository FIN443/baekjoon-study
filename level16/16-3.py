from collections import Counter
import sys

input = sys.stdin.readline
counter = Counter()

S = input()
q = int(input())
acc = [("", 0)]
for i in S:
    counter[i] += 1
    acc.append((i, counter[i]))

for _ in range(q):
    word, i, j = input().split()
    a, b = map(int, [i, j])
    n1 = 0
    n2 = 0
    for i in acc[b + 1 :: -1]:
        if i[0] == word:
            n1 = i[1]
            break
    for i in acc[a::-1]:
        if i[0] == word:
            n2 = i[1]
            break
    print(n1 - n2)
