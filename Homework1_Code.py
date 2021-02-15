import random

def player():
    while True:
        playerInput = str(input("Enter your choice: Rock (R), Paper (P), Scissors (S), Lizard (L), Spock (V): "))
        if playerInput in ("R", "P","S","L","V"):
            break
        else:
            print("Invalid input. Try again.")
    return playerInput

def computer():
    computerChoices = ["R", "P","S","L","V"]
    computerInput = random.choice(computerChoices)
    return  computerInput

def game():
    print("Game: rock, paper, scissors, lizard, Spock")
    playerChoice = player()
    computerChoice = computer()
    while True:
        if playerChoice == computerChoice:
            print("Draw! Try again.")
        elif playerChoice == "S" and computerChoice == "P":
            print("You win!")
            print("Scissors cuts Paper")
            return True
        elif playerChoice == "P" and computerChoice == "R":
            print("You win!")
            print("Paper covers Rock")
            return True
        elif playerChoice == "R" and computerChoice == "L":
            print("You win!")
            print("Rock crushes Lizard")
            return True
        elif playerChoice == "L" and computerChoice == "V":
            print("You win!")
            print("Lizard poisons Spock")
            return True
        elif playerChoice == "V" and computerChoice == "S":
            print("You win!")
            print("Spock smashes Scissors")
            return True
        elif playerChoice == "S" and computerChoice == "L":
            print("You win!")
            print("Scissors decapitates Lizard")
            return True
        elif playerChoice == "L" and computerChoice == "P":
            print("You win!")
            print("Lizard eats Paper")
            return True
        elif playerChoice == "P" and computerChoice == "V":
            print("You win!")
            print("Paper disproves Spock")
            return True
        elif playerChoice == "V" and computerChoice == "R":
            print("You win!")
            print("Spock vaporizes Rock")
            return True
        elif playerChoice == "R" and computerChoice == "S":
            print("You win!")
            print("Rock crushes Scissor")
            return True
        
        elif computerChoice == "S" and playerChoice == "P":
            print("You lose!")
            print("Scissors cuts Paper")
            return False
        elif computerChoice == "P" and playerChoice == "R":
            print("You lose!")
            print("Paper covers Rock")
            return False
        elif computerChoice == "R" and playerChoice == "L":
            print("You lose!")
            print("Rock crushes Lizard")
            return False
        elif computerChoice == "L" and playerChoice == "V":
            print("You lose!")
            print("Lizard poisons Spock")
            return False
        elif computerChoice == "V" and playerChoice == "S":
            print("You lose!")
            print("Spock smashes Scissors")
            return False
        elif computerChoice == "S" and playerChoice == "L":
            print("You lose!")
            print("Scissors decapitates Lizard")
            return False
        elif computerChoice == "L" and playerChoice == "P":
            print("You lose!")
            print("Lizard eats Paper")
            return False
        elif computerChoice == "P" and playerChoice == "V":
            print("You lose!")
            print("Paper disproves Spock")
            return False
        elif computerChoice == "V" and playerChoice == "R":
            print("You lose!")
            print("Spock vaporizes Rock")
            return False
        elif computerChoice == "R" and playerChoice == "S":
            print("You lose!")
            print("Rock crushes Scissor")
            return False
