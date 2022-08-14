# 안정적인 문자열
page = 1
while True:
    vps = input()
    count = 0
    if "-" in vps:
        exit()

    stack = []
    for i in vps:
        if not stack and i == "}":
            count += 1
            stack.append("{")
        elif stack and i == "}":
            stack.pop()
        else:
            stack.append(i)

    count += len(stack) // 2
    print(f"{page}. {count}")
    page += 1
