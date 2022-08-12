# 천재 수학자 성필
prefix = input()

oper = []
for i in prefix:
    if i.isdigit():
        oper.append(int(i))
    else:
        v1 = oper.pop()
        v2 = oper.pop()

        if i == "+":
            oper.append(v2 + v1)
        elif i == "-":
            oper.append(v2 - v1)
        elif i == "*":
            oper.append(v2 * v1)
        elif i == "/":
            oper.append(v2 // v1)

print(oper[0])
