def change_word(b_pos, start_word):
    global board
    word_len = b_pos - start_word
    pos = start_word
    while word_len > 0:
        if word_len >= 4:
            board = board[:pos] + "AAAA" + board[pos + 4 :]
            pos += 4
            word_len -= 4
        else:
            board = board[:pos] + "BB" + board[pos + 2 :]
            pos += 2
            word_len -= 2

    return word_len


board = input()
end = len(board)
b_pos = 0
start_word = 0
isWord = False
check = True

while b_pos < end:
    if not isWord and board[b_pos] == "X":
        start_word = b_pos
        isWord = True

    if isWord and board[b_pos] == ".":
        word_len = change_word(b_pos, start_word)
        if word_len != 0:
            check = False
        isWord = False

    if isWord and b_pos == end - 1:
        word_len = change_word(b_pos + 1, start_word)
        if word_len != 0:
            check = False
        isWord = False

    b_pos += 1

if not check:
    print(-1)
else:
    print(board)


""" 날 먹
board=str(input())
board=board.replace("XXXX","AAAA")
board=board.replace("XX","BB")

if "X" in board:
  print(-1)
else:
  print(board)
"""
