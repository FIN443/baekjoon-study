N = int(input())
a = N // 2
b = N // 5
c = N // 25
d = N // 125

if a > b + c + d:
    print(a)
else:
    print(b + c + d)
