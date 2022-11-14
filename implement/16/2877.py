# 4와 7
K = int(input())
s = format(K + 1, "b")
s = s[1:].replace("0", "4").replace("1", "7")
print(s)
