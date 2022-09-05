# 단어 뒤집기 2
words = list(input())

end = len(words)
prev = 0
pos = 0
state = False

while pos < end:
    if not state and words[pos] == " ":
        temp = words[prev:pos]
        words[prev:pos] = temp[::-1]
        prev = pos + 1
    elif words[pos] == "<":
        temp = words[prev:pos]
        words[prev:pos] = temp[::-1]
        prev = pos + 1
        state = True
    elif words[pos] == ">":
        prev = pos + 1
        state = False

    pos += 1

if pos == end and pos != prev:
    temp = words[prev:pos]
    words[prev:pos] = temp[::-1]

print("".join(words))
