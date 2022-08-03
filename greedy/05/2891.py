N, _, _ = map(int, input().split())
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))

plus_ = sorted(plus)

for i in plus_:
    if i in minus:
        minus.pop(minus.index(i))
        plus.pop(plus.index(i))
        continue
    for j in (i - 1, i, i + 1):
        if j in minus:
            minus.pop(minus.index(j))
            plus.pop(plus.index(i))
            break

print(len(minus))

""" 반례(스페어를 박살냄)
5 2 2
1 2
2 3 
"""
