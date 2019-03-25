def play_game():
    player1Selection = input(
        "Player 1, Please type Paper, Rock or Scissors:  ").capitalize()
    player2Selection = input(
        "Player 1, Please type Paper, Rock or Scissors:  ").capitalize()

    try:
        type(player1Selection) and type(player2Selection) == str


    if player1Selection == 1 and player2Selection == 2:
        print("Paper beats Rock! Player 1 wins!")
    elif player1Selection == 2 and player2Selection == 3:
        print("Rock beats Scissors! Player 1 wins!")
    elif player1Selection == 3 and player2Selection == 1:
        print("Scissors beats Paper! Player 1 wins!")
    elif player2Selection == 1 and player1Selection == 2:
        print("Paper beats Rock! Player 2 wins!")
    elif player2Selection == 2 and player1Selection == 3:
        print("Rock beats Scissors! Player 2 wins!")
    elif player2Selection == 3 and player1Selection == 1:
        print("Scissors beats Paper! Player 2 wins!")
    else:
        print("You both picked the same item, and tied!")

    playagain = input("Would you like to play again?  Enter y to play again or any other key to exit.")
    if playagain.lower() == 'y':
        play_game()
    else:
        print("Goodbye!")
        return 1    

play_game()