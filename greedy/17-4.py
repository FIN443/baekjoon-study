mod = input().split("-")
plus = list(map(int, mod.pop(0).split("+")))
minus = []
for i in mod:
    minus += list(map(int, i.split("+")))
print(sum(plus) - sum(minus))
