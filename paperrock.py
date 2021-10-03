from random import choice #to select a random element from the list 
import sys

choices = ["paper", "scissors", "rock"]
u1_answer = input("Choose paper, scisscors or rock: ")
u2_answer = choice(choices)
print ("The computes chooses to play", u2_answer)

def compare (choices, x):
    if choices == x:
        return ("You both choose "+ x+ "!")
        
    elif choices == 'paper':
        if x == 'scissors':
            return ("The computer chose "+ u2_answer + ", you win!")
        else:
            return ("The computer chose "+ u2_answer+ ", you lose!")

    elif choices == 'scissors':
        if x == 'paper':
            return ("The computer chose "+ u2_answer+ ", you lose!")
        else:
            return ("The computer chose "+ u2_answer+ ", you win!")
            
    elif choices == 'rock':
        if x == 'paper':
            return("The computer chose "+ u2_answer+ ", you win!")
        else:
            return ("The computer chose "+ u2_answer+ ", you lose!")
                
    else:
        return ("Invalid input! You must have made a spelling mistake.")
        sys.exit
        
print(compare(u1_answer, u2_answer))
