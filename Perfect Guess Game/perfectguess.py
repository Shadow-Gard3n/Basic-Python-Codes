def repeat():
    print("!!YOU NEED TO GUESS THE NUMBER CHOOSEN BY COMPUTER IN MINIMUM ROUNDS!!")
    print("HINT: NUMBER IS BETWEEN 1 AND 100")
    import random
    a = random.randint(1,100)
    b = int(input("\nWrite the number you think has been choosen by computer: "))
    if b >= 1 and b <= 100:
        pass
    else:
        print("Wrong input please try again")
        repeat()
    z = 0
    while a != b:
        if a > b:
            print("\nWrong guess")
            print(f"HINT: The number is greater than {b}")
            
        elif b > a:
            print("\nWrong guess")
            print(f"HINT: The number is smaller than {b}")
        z = z + 1
        print(f"ROUND: {z}")
        b = int(input("\nWrite the number you want to guess between 1 and 100: "))
    if a == b:
        print("!!!You guessed it correct!!!")
        score = 100-z
        print(f"SCORE: {score} ")
        print(f"You took {z+1} rounds to guess it.")
    else:
        pass
    with open("highscore.txt","r") as f:
        hs = f.read()
    if score > int(hs):
        with open("highscore.txt","w") as f:
            f.write(str(score))
        print("\n!!! A NEW HIGH SCORE !!!")
    else:
        pass   
    choice()
def choice():
        y = input("Press 1 for exit and 2 for retry and 3 for highscore: ")
        if y == "1":
            exit()
        elif y == "2":
            repeat()
        elif y == "3":
            with open("highscore.txt","r") as f:
                highscore = f.read()  
            print(highscore)
            choice()
        else:
            print("Wrong input, please try again")
            choice()       
repeat()

    
    
    
