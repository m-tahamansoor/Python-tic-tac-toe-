def box(values):
    print("\n")
    print("\t       |     |          ")
    print(f"\t    {values[0]}  |  {values[1]}  |  {values[2]}")
    print("\t   ----|-----|----")
    print(f"\t    {values[3]}  |  {values[4]}  |  {values[5]}")
    print("\t   ----|-----|----")
    print(f"\t    {values[6]}  |  {values[7]}  |  {values[8]}")
    print("\t       |     |          ")
    print("\n")

def check_win(player, cur_player):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in soln:
        if all(y in player[cur_player] for y in x):
            return True
    return False

def print_scoreboard(score_board):
    print("\t---------------------------------")
    print("\t              SCOREBOARD      ")
    print("\t---------------------------------")
    
    players = list(score_board.keys())
    print(f"\t   {players[0]}   \t   {score_board[players[0]]}")
    print(f"\t   {players[1]}   \t   {score_board[players[1]]}")

    print("\t---------------------------------\n")

def check_draw(player):
    if len(player['X']) + len(player['0']) == 9:
        return True
    return False
    
def single_player(cur_player):
    global player
    values = [" " for _ in range(9)]
    player = {"X": [], "0": []}
    
    while True:
        box(values)
        try:
            print(f"Player {cur_player}'s turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong input")
            continue
        
        if move < 1 or move > 9:
            print("Wrong input")
            continue
        
        if values[move - 1] != " ":
            print("Place is already filled")
            continue
        
        values[move - 1] = cur_player
        player[cur_player].append(move)
        
        if check_win(player, cur_player):
            box(values)
            print(f"Player {cur_player} has won the game!!\n")
            return cur_player
        
        if check_draw(player):
            box(values)
            print("Game Drawn\n")
            return 'D'
        
        cur_player = '0' if cur_player == 'X' else 'X'

if __name__ == "__main__":
    print("Player 1")
    player1 = input("Enter the name: ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name: ")
    print("\n")

    score_board = {player1: 0, player2: 0}
    cur_player = player1

    player_choice = {'X': "", '0': ""}
    options = ['X', '0']
    
    while True:
        print(f"Turn to choose for {cur_player}")
        print("Enter 1 for X")
        print("Enter 2 for 0")
        print("Enter 3 to Quit")

        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        if choice == 1:
            player_choice['X'] = cur_player
            player_choice['0'] = player2 if cur_player == player1 else player1

        elif choice == 2:
            player_choice['0'] = cur_player
            player_choice['X'] = player2 if cur_player == player1 else player1

        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break
        
        else:
            print("Wrong Choice!!!! Try Again\n")
            continue

        winner = single_player(options[choice - 1])

        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] += 1

        cur_player = player2 if cur_player == player1 else player1
