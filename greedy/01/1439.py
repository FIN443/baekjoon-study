S = input()
end = len(S)

pos = 0
zero_flip = 0
front_zero = False
while pos < end:
    if not front_zero and S[pos] == "0":
        zero_flip += 1
        front_zero = True

    elif front_zero and S[pos] == "1":
        front_zero = False

    pos += 1

pos = 0
one_flip = 0
front_one = False
while pos < end:
    if not front_one and S[pos] == "1":
        one_flip += 1
        front_one = True

    elif front_one and S[pos] == "0":
        front_one = False

    pos += 1

print(min(zero_flip, one_flip))
