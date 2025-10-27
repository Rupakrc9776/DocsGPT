# tictactoe.py
def print_board(b):
    for i in range(3):
        print(" | ".join(b[i]))
        if i < 2: print("---------")

def check(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != " ": return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != " ": return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != " ": return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != " ": return b[0][2]
    return None

b = [[" "]*3 for _ in range(3)]
player = "X"
for _ in range(9):
    print_board(b)
    r, c = map(int, input(f"Player {player}, enter row col (0-2): ").split())
    if b[r][c] == " ":
        b[r][c] = player
        if check(b):
            print_board(b)
            print(f"🎉 Player {player} wins!")
            break
        player = "O" if player == "X" else "X"
else:
    print("It's a tie!")
