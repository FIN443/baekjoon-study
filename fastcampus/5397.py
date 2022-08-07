# 키로거
T = int(input())
for _ in range(T):
    password = input()
    word = []
    bakup = []
    for i in password:
        if word and i == "<":
            bakup.append(word.pop())
        elif bakup and i == ">":
            word.append(bakup.pop())
        elif word and i == "-":
            word.pop()
        elif i != "<" and i != ">" and i != "-":
            word.append(i)
    word.extend(reversed(bakup))  # 남은것들 합쳐야 함
    print("".join(word))
