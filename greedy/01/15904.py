import sys

input = sys.stdin.readline
s = input()
target = "UCPC"
isCheck = True

for i in target:
    if i in s:
        s = s[s.find(i) + 1 :]  # 이후 문장으로 갱신
    else:
        isCheck = False
        break

if isCheck:
    print("I love UCPC")
if not isCheck:
    print("I hate UCPC")
