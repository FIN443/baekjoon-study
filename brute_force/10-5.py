N = int(input())

s = 666
count = 0
while True:
    if "666" in str(s):
        count += 1
        if count == N:
            print(s)
            break
    s += 1

""" 다른 답안
n = int(input())

answer = []
i = 0
while True:
    if len(answer) == n:
        break
    if '666' in str(i):
        answer.append(i)
    i += 1
print(answer[-1])
"""
