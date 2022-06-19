def getTwo(n):
    x = 0
    mul = 2
    while mul <= n:
        x += n // mul
        mul *= 2
    return x


def getFive(n):
    x = 0
    mul = 5
    while mul <= n:
        x += n // mul
        mul *= 5
    return x


a, b = map(int, input().split())
# aCb -> a! / (a-b)! b!

n1 = getTwo(a) - getTwo(a - b) - getTwo(b)
n2 = getFive(a) - getFive(a - b) - getFive(b)

if n1 > n2:
    print(n2)
else:
    print(n1)
