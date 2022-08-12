# 후위 표기식2
N = int(input())
prefix = input()
nums = []
for i in range(N):
    nums.append(int(input()))

oper = []
for i in prefix:
    if i.isalpha():
        oper.append(nums[ord(i) - 65])
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
            oper.append(v2 / v1)

print(f"{oper[0]:.2f}")
