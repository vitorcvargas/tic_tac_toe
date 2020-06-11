from modules import GameTable

table = GameTable()




def game_on():

    player1_mark = input('Player one, pick "X" or "O" for your mark:\n')
    if player1_mark.upper() == "X":
        player2_mark = "O"
    else:
        player2_mark = "X"

    counter = 0

    game_on = True    
    while game_on: 

        player1_turn = True
        while player1_turn:

            print("It's your turn, player 1")
            print(table)
            print()
            print()

            while True:
                player1_choice = input('Choose your next move: ')
                if table.add(player1_choice, player1_mark) == False:
                    print("Try again with an available block")
                else:
                    table.add(player1_choice, player1_mark)
                    counter += 1
                    break

            if table.result(counter) == True:
                print("Player 1 wins!")
                game_on = False
                player1_turn = False

            elif table.result(counter) == False:
                print("It's a draw")
                game_on = False
            else:
                player1_turn = False
                break
            break
        
        if game_on == False:
            player2_turn = False
        else:
            player2_turn = True
        while player2_turn:
            print("It's your turn, player 2")
            print(table)

            while True:
                player2_choice = input('Choose your next move: ')
                if table.add(player2_choice, player2_mark) == False:
                    print("Try again with an available block")
                else:
                    table.add(player2_choice, player2_mark)
                    counter += 1
                    break
                        
            if table.result(counter) == True:
                print("Player 2 wins!")
                player2_turn = False
                game_on = False

            elif table.result(counter) == False:
                print("It's a draw")
                player2_turn = False
                game_on = False
            else:
                player2_turn = False
                break
            break
        if game_on == True:
            player1_turn = True
        else:
            player1_turn = False

            play_again = input("Do you want to play again? y/n")
            if play_again.lower() == 'y':
                game_on = True
                for block in table.blocks:
                    table.blocks[block] = ""
                counter = 0

game_on()
                

            
