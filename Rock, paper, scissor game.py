import random
#rock, paper, scissor
print("Welcome to rock, paper, scissor game!")
op = ("Rock", "Paper", "Scissor") #tupple cointaning the available moves
print("The game will continue for 5 rounds")
i = 0 #for the amount of time the loop will run
u = 0 #counter for how many rounds user won
p = 0 #counter for how many rounds ai won
while i < 5 :
    user = input("Your move : ")
    a = random.randint(0,2)
    ai = op[a] #creating a variable to randomly choose the available option as the ai's next move
    if user == "Scissor" and ai == "Paper" :
        print("Ai : ", ai)
        print("You win this round \n")
        u = u + 1
    elif user == "Scissor" and ai == "Rock" :
        print("Ai : ", ai)
        print("Ai wins this round \n")
        p = p + 1
    elif user == "Scissor" and ai == "Scissor" :
        print("Ai : ", ai)
        print("Tie \n")
    elif user == "Rock" and ai == "Rock" :
        print("Ai : ", ai)
        print("Tie \n")
    elif user == "Rock" and ai == "Paper" :
        print("Ai : ", ai)
        print("Ai wins this round \n")
        p = p + 1
    elif user == "Rock" and ai == "Scissor" :
        print("Ai : ", ai)
        print("You win this round \n")
        u = u + 1
    elif user == "Paper" and ai == "Rock" :
        print("Ai : ", ai)
        print("You win this round \n")
        u = u + 1
    elif user == "Paper" and ai == "Scissor" :
        print("Ai : ", ai)
        print("Ai wins this round \n")
        p = p + 1
    elif user == "Paper" and ai == "Paper" :
        print("Ai : ", ai)
        print("Tie \n")
    else :
        print("Enter proper input and no retries in these rounds \n")
    i = i + 1
    if i == 5 : #for printing the final conclusion of this game
        if u>p :
            print("You win this game!")
        elif u<p :
            print("Ai wins this game :(")
            print("Better luck next time")
        else :
            print("There's a tie")
