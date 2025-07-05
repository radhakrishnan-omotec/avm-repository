import os
from test3 import print_board, win_check
B = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

print_board(B)

for i in range(9):
    while True:
        x = int(input("Enter a position: "))
        if B[x-1] == ' ':
            break
        print ("Cannot place there... ")
    if i%2 == 0:
        B[x-1] = 'X'
    else:
        B[x-1] = 'O'
    os.system('cls')
    print_board(B)
    win = win_check(B)
    if win == "X wins!":
        print ("X won the game")
        break
    if win == "O wins!":
        print ("O won the game")
        break

if win!= 'X wins! ' and win!= 'O wins! ':
    print ("It's a draw")