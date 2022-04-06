a, b = input().split()
a = int(a)
b = int(b)

if b < 45:
    if a == 0:
        h = 23
    else:
        h = a - 1
    m = 60 - (45 - b)
else:
    h = a
    m = b - 45

print(h, m)
