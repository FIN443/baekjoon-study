# A와 B
S = input()
T = input()

cond = False
while T:
    if T[-1] == "A":
        T = T[:-1]
    elif T[-1] == "B":
        T = T[-2::-1]
    if S == T:
        cond = True
        break

if cond:
    print(1)
else:
    print(0)
