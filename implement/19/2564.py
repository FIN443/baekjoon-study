# 경비원

w, h = map(int, input().split())
n = int(input())
lst = []
for _ in range(n + 1):
    lst.append(list(map(int, input().split())))

pos, target = lst[:-1], lst[-1]

result = 0
for d, l in pos:
    if target[0] == 1:
        if d == 1:
            result += abs(target[1] - l)
        elif d == 2:
            result += min(target[1] + h + l, (w - target[1]) + h + (w - l))
        elif d == 3:
            result += target[1] + l
        elif d == 4:
            result += (w - target[1]) + l
    elif target[0] == 2:
        if d == 1:
            result += min(target[1] + h + l, (w - target[1]) + h + (w - l))
        elif d == 2:
            result += abs(target[1] - l)
        elif d == 3:
            result += target[1] + (h - l)
        elif d == 4:
            result += (w - target[1]) + (h - l)
    elif target[0] == 3:
        if d == 1:
            result += target[1] + l
        elif d == 2:
            result += (h - target[1]) + l
        elif d == 3:
            result += abs(target[1] - l)
        elif d == 4:
            result += min(target[1] + w + l, (h - target[1]) + w + (h - l))
    elif target[0] == 4:
        if d == 1:
            result += target[1] + (w - l)
        elif d == 2:
            result += (h - target[1]) + (w - l)
        elif d == 3:
            result += min(target[1] + w + l, (h - target[1]) + w + (h - l))
        elif d == 4:
            result += abs(target[1] - l)

print(result)
