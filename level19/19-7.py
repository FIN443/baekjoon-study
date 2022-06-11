from collections import deque


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    lst = input().strip("[]").split(",")
    deq = deque(lst)
    if n == 0:
        deq = deque()
    error = False
    reverse = False
    for order in p:
        if order == "R":
            if reverse == False:
                reverse = True
            else:
                reverse = False
        elif order == "D":
            if not deq:
                error = True
                print("error")
                break
            else:
                if reverse == True:
                    deq.pop()
                elif reverse == False:
                    deq.popleft()
    if error:
        continue
    else:
        if not reverse:
            print("[", end="")
            print(*deq, sep=",", end="]\n")
        elif reverse:
            deq.reverse()
            print("[", end="")
            print(*deq, sep=",", end="]\n")
