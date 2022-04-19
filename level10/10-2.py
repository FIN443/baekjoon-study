N = input()
gen = 0
result = 0
results = []
for i in range(int(N), 0, -1):
    num = str(i)
    line = len(str(i))
    for j in range(line):
        result += int(num[j])
        gen += int(num[j]) * (10 ** (line - j - 1))
    result += gen
    if int(N) == result:
        results.append(gen)
    gen = 0
    result = 0
if results:
    print(results[-1])
else:
    print(0)
