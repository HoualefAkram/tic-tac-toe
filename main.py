line1, line2, line3, round_number = ["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"], 0
print(f"{line1}\n{line2}\n{line3}")
game = [line1, line2, line3]


def winner():
    for s, j, k in zip(line1, line2, line3):
        if s == j == k == "X" or s == j == k == "O":
            return True
    for f in game:
        if f[0] == f[1] == f[2] == "X" or f[0] == f[1] == f[2] == "O":
            return True
    if line1[0] == line2[1] == line3[2] == "X" or line1[0] == line2[1] == line3[2] == "O" or line1[2] == line2[1] == \
            line3[0] == "X" or line1[2] == line2[1] == line3[0] == "O":
        return True
    return False


for i in range(9):  # main loop
    line, column, answer = int(input("enter line :")), int(input("enter column : ")), input("X,O :")
    game[line - 1][column - 1] = answer.upper()
    print(f"{line1}\n{line2}\n{line3}")
    round_number = i
    if winner():
        if i % 2 == 0:
            print("player 1 Won!")
            break
        else:
            print("player 2 Won!")
            break
if round_number == 8:
    print("Draw!")