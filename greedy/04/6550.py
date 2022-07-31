while True:
    try:
        s, t = input().split()
        isCheck = True
        for i in s:
            # print(i, idx, t)
            if i in t:
                t = t[t.find(i) + 1 :]
            else:
                isCheck = False
                break
        if isCheck:
            print("Yes")
        else:
            print("No")
    except:
        break
