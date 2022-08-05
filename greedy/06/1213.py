from collections import Counter

s = list(input())
s_ = Counter(s)
s_ = sorted(list(s_.items()), key=lambda x: x[0])

half = ""
center = ""
for alpha, count in s_:
    if count % 2 == 1:
        center = alpha
        count -= 1
    half += alpha * (count // 2)

new_s = half + center + half[::-1]
if len(new_s) == len(s):
    print(new_s)
else:
    print("I'm Sorry Hansoo")
