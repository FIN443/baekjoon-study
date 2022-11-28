# 틱택토
def solution(ttt, typ):
    if ttt[0] == typ and ttt[0] == ttt[1] == ttt[2]:
        return True
    elif ttt[0] == typ and ttt[0] == ttt[3] == ttt[6]:
        return True
    elif ttt[4] == typ and ttt[1] == ttt[4] == ttt[7]:
        return True
    elif ttt[4] == typ and ttt[3] == ttt[4] == ttt[5]:
        return True
    elif ttt[8] == typ and ttt[6] == ttt[7] == ttt[8]:
        return True
    elif ttt[8] == typ and ttt[2] == ttt[5] == ttt[8]:
        return True
    elif ttt[4] == typ and ttt[0] == ttt[4] == ttt[8]:
        return True
    elif ttt[4] == typ and ttt[2] == ttt[4] == ttt[6]:
        return True
    else:
        return False


while True:
    ttt = input()
    if ttt == "end":
        break
    x_count = ttt.count("X")
    o_count = ttt.count("O")

    if x_count == o_count + 1 or x_count == o_count:
        if x_count == o_count + 1:
            case1, case2 = "X", "O"
        else:
            case1, case2 = "O", "X"
        result1 = solution(ttt, case1)
        result2 = solution(ttt, case2)

        if result2:
            print("invalid")
        elif not result1:
            if ttt.count(".") == 0:
                print("valid")
            else:
                print("invalid")
        else:
            print("valid")
    else:
        print("invalid")
