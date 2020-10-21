from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    # Plays a guessing game with the user.
    def __init__(self):
        # Sets up the window and the widgets.
        EasyFrame.__init__(self, title = "Guessing Game", width = 800)

        # Initialize the instance variables for the data
        self.myNumber = random.randint(1, 10)
        self.count = 0

        #  Create and add widgets to the window
        greeting = "Guess a number between 1 and 10."
        self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0, sticky = "NSEW", columnspan = 2)
        self.addLabel(text = "Your guess:", row = 1, column = 0)

        self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)

        # Command Buttons
        self.nextButton = self.addButton(text = "Next", row = 2, column = 0, command = self.nextGuess)
        self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)

    # Event handling functions
    def nextGuess(self):
        # Processes the user's next guess
        self.count += 1
        guess = self.guessField.getNumber()
        # Logic to determine the game result
        if guess == self.myNumber:
            self.hintLabel["text"] = "You won! You've guessed it in " + str(self.count) + " attempts!"
            self.nextButton["state"] = "disabled"
        elif guess < self.myNumber:
            self.hintLabel["text"] = "Sorry, guess was too low."
        else:
            self.hintLabel["text"] = "Whoops, guess was too high."
    
    def newGame(self):
        # Resets the game data and GUI to their original states
        self.myNumber = random.randint(1, 10)
        self.count = 0
        greeting = "guess a number between 1 and 10"
        self.hintLabel["text"] = greeting
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"

# definition of the main() function
def main():
    GuessingGame().mainloop()
# Global call to the main() function
main()
