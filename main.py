import random

def guessing():
    difficulties = {
        1: {"name": "Hard", "chances": 3, "hint_turn": 1, "hint_range": 2},
        2: {"name": "Medium", "chances": 6, "hint_turn": 3, "hint_range": 3},
        3: {"name": "Easy", "chances": 10, "hint_turn": 5, "hint_range": 4}
    }

    while True:
        try:
            choices = int(input("Pick a difficulty: \n"
                "1. Hard\n"
                "2. Medium\n"
                "3. Easy\n"))
            settings = difficulties[choices]
            print(f"You get {settings['chances']} chances")
            break
        except:
            print("Pick 1-3")
            
    randomNum = random.randint(1,100)
    print(randomNum)

    i = 0
    while i < settings['chances']:
        i+=1

        while True:
            try:
                userGuess = int(input("Enter your guess: \n"))
                break
            except ValueError:
                print("Invalid Input")

        if userGuess == randomNum:
            print(f"Congrats, It took you {i} time(s)")
            break

        if userGuess < randomNum:
            print("Guess higher")
        else:
            print("Guess lower")

        if i == settings['hint_turn']:
            print(f"Number is between {randomNum - settings['hint_range']} and {randomNum + settings['hint_range']}")
    else:
        print("Run out of guesses")

    while True:
        try:
            playAgain = int(input("Would you like to play again?: \n" \
                "1. Yes \n" \
                "2. No \n"))
            return playAgain
        except:
            print("Pick 1-2")

playAgain = guessing()
if playAgain == 1:
    guessing()
else:
    print("Game Terminated")