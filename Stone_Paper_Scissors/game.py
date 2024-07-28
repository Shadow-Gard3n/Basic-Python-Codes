
def your_choice():
    print("So will you choose stone, paper or scissors?")
    b = int(input("Press '1' for stone and '2' for paper and '3' for scissors: "))
    if b == 1:
        yourchoice = "Stone"
    elif b == 2:
        yourchoice = "Paper"
    elif b == 3:
        yourchoice = "Scissors"
    else:
        print("Wrong input, please try again")
        your_choice()
    return yourchoice
    
def computer_choice(): 
    import random
    c = random.randint(1,3)
    if c == 1:
            computerchoice = "Stone"
    elif c == 2: 
        computerchoice = "Paper"
    elif c == 3:
        computerchoice = "Scissors"
    else:
        pass
    return computerchoice




def game():
    yourchoice = your_choice()
    computerchoice = computer_choice()
    
    
    if yourchoice == "Stone":
        if computerchoice == "Stone":
            winner = "none"
            print("!!A TIE!!")
        elif computerchoice == "Paper":
            winner = "computer"
            print("!!YOU LOSE!!")
        elif computerchoice == "Scissors":
            winner = "you"
            print("!!YOU WIN!!")

    elif yourchoice == "Paper":
        if computerchoice == "Paper":
            print("!!A TIE!!")
            winner = "none"
        elif computerchoice == "Scissors":
            winner = "computer"
            print("!!YOU LOSE!!")
        elif computerchoice == "Stone":
            winner = "you"
            print("!!YOU WIN!!")
       
    elif yourchoice == "Scissors":
        if computerchoice == "Scissors":
            winner = "none"
            print("!!A TIE!!")
        elif computerchoice == "Stone":
            winner = "computer"
            print("!!YOU LOSE!!")
        elif computerchoice == "Paper":
            winner = "you"
            print("!!YOU WIN!!")
        
    print("Your choice: ",yourchoice)
    print("Computer choice: ",computerchoice)
    return winner


def loop():

    print("!!!Try to win 5 times in lesser round!!!")

    def main():

        victory = 0
        not_victory = 0
        while victory < 5:


            winner = game()

            if winner == "you":
                victory = victory + 1
                print("ROUND: ", victory + not_victory)
                print("VICTORY: ",victory)
            else:
                not_victory = not_victory + 1
                print("ROUND: ", victory + not_victory)
                print("VICTORY: ",victory)

        if victory == 5:
            x = 105 - (victory + not_victory)
            print("Your score is", x)
        else:
            pass
        return x        

    x = main()

    with open("highscore.txt", "r") as h:
        n = h.read()

    if x > int(n):
        with open("highscore.txt","w") as h:
            h.write(str(x))
        print("!!! NEW HIGH SCORE !!!")
    else:
        pass


    def end():
        y = int(input("Press 1 for retry and 2 to end this and 3 to view the high score: "))
        if y == 1:
            loop()
        elif y == 2:
            exit()
        elif y == 3:
            with open("highscore.txt") as h:
                g = h.read()
                print(g)
            end()
        else:
            print("Wrong input, so retry")
            end()
    end()

loop()
    

        

        
        

            

