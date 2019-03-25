def play_game():
    try:
        player1Selection = int(input("Player 1, Please select one of the following:\n1.) Paper\n2.) Rock\n3.) Scissors\n\n(Enter 1, 2 or 3): "))
    except ValueError:
        print("You must inter an interger (1 - 3)")
    except UnboundLocalError:
        print("Make sure you enter 1, 2 or 3")
        #return 1
    try:
        player2Selection = int(input("Player 2, Please select one of the following:\n1.) Paper\n2.) Rock\n3.) Scissors\n\n(Enter 1, 2 or 3): "))
    except ValueError:
        print("Value Error Eric")
    except UnboundLocalError:
        print("Make sure you enter 1, 2 or 3")
        #return 1
    
    if player1Selection in range(1,4) and player2Selection in range(1,4):
        pass
    else:
        print("must be 1 2 or 3")
        #return 1

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
        #return 1

play_game()