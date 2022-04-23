N = input()
lst = []
for i in N:
    lst.append(int(i))
lst = sorted(lst, reverse=True)
result = ""
for i in lst:
    result += str(i)
print(result)

""" 개쩌는 답안
[print(x, end="") for x in sorted(list(input()), reverse=True)]
"""
