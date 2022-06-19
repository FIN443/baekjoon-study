import re


lst = []
S = ""
while True:
    S = input()
    if S == ".":
        break
    else:
        lst.append(S)
for s in lst:
    vps = re.findall("[(\)[\]]", s)
    stack = []
    for i in vps:
        if stack and i == ")" and stack[-1] == "(":
            stack.pop()
        elif stack and i == "]" and stack[-1] == "[":
            stack.pop()
        else:
            stack.append(i)
    if stack:
        print("no")
    else:
        print("yes")
