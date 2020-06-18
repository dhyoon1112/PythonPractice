
print("Welcome to Rock Paper Scissors. Player 1 enters their choice first, and then Player 2")
player1 = input("Player 1 enter Rock, Paper, or Scissors: " )
player2 = input("Player 2 enter Rock, Paper, or Scissors: " )

Victor = 0
while (Victor == 0):

    #Player1
    if player1 == "Rock" and player2 == "Scissors":
        print("Player 1 wins")
        Victor = 1
    elif player1 == "Scissors" and player2 == "Paper":
        print("Player 1 wins")
        Victor = 1
    elif player1 == "Paper" and player2 == "Rock":
        print("Player 1 wins")
        Victor = 1

    #Player2
    elif player2 == "Rock" and player1 == "Scissors":
        print("Player 2 wins")
        Victor = 1
    elif player2 == "Scissors" and player1 == "Paper":
        print("Player 2 wins")
        Victor = 1
    elif player2 == "Paper" and player1 == "Rock":
        print("Player 2 wins")
        Victor = 1

    #Tie
    elif player1 == player2:
        print("You tied, try again")
        player1 = input("Player 1 enter Rock, Paper, or Scissors: " )
        player2 = input("Player 2 enter Rock, Paper, or Scissors: " )

    #Invalid
    elif player1 != player2:
        print("Invalid Entry")
        player1 = input("Player 1 enter Rock, Paper, or Scissors: " )
        player2 = input("Player 2 enter Rock, Paper, or Scissors: " )
