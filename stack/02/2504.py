# 괄호의 값
word = input()
stack = []
result = 0
temp = 1
for i in range(len(word)):
    if word[i] == "(":
        stack.append(word[i])
        temp *= 2
    elif word[i] == "[":
        stack.append(word[i])
        temp *= 3
    elif word[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if word[i - 1] == "(":
            result += temp
        stack.pop()
        temp //= 2
    elif word[i] == "]":
        if not stack or stack[-1] == "(":
            result = 0
            break
        if word[i - 1] == "[":
            result += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(result)
