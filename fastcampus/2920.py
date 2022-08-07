# 음계
lst = list(map(int, input().split()))

isAscending = True
if lst[0] > lst[1]:
    isAscending = False

isMixed = False
for i, j in zip(lst, lst[1:]):
    if isAscending and i > j:
        isMixed = True
        break
    elif not isAscending and i < j:
        isMixed = True
        break

if isMixed:
    print("mixed")
else:
    if isAscending:
        print("ascending")
    else:
        print("descending")
