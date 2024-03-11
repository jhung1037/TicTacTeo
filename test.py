
board = ""
for i in range(1, 10):
    if i == 9:
        board += str(i) + "\n"
    elif i == 3 or i == 6:
        board += str(i) + "\n- + - + -\n"
    else:
        board += str(i) + " | "
print(board)