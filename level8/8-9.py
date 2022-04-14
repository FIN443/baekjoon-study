# Case 1
""" while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    if z**2 != x**2 + y**2 and y**2 != x**2 + z**2 and x**2 != y**2 + z**2:
        print("wrong")
    elif x == y == z == 1:
        print("wrong")
    else:
        print("right") """

# Case 2
while True:
    x, y, z = sorted(list(map(int, input().split())))
    if x == y == z == 0:
        break
    if z**2 != x**2 + y**2 and y**2:
        print("wrong")
    elif x == y == z == 1:
        print("wrong")
    else:
        print("right")
