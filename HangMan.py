import random

# This is a simple hangman game. You can find a general description in the README.

# Variable descriptions:
#   word: the actual word the player is trying to guess
#   length: the length of 'word', it is used for determining winning conditions and other variable lengths
#   attempts: the amount of 'lives', 'tries', or attempts that the player has to guess the letters in the 'word'
#   win_condition: a boolean that is set to True when the player wins. Initially False.
#   winning_letters: the amount of letters the player needs to guess to win. Used in determining 'win_condition"
#   letters_to_guess: the letters that the player can guess from.
#   shown_word: this is the usual part of the word the player sees in a normal hangman game. (i.e. the _ _ _ e _ t)
#   word_list: a list of words in the english dictionary obtained from a file downloaded from the internet. Will get
#               source as soon as I find it.as

# Above each function you will find a description of what it does.

class HangMan:

    word = ""
    length = 0
    attempts = 0
    win_condition = False
    winning_letters = 0
    letters_to_guess = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
    shown_word = []
    word_list = []

    #  the usual init function.  This sets up the game.  I will probably move most of what is in this to another
    #  function to improve readability and make more logical sense down the line.
    #  What this does is it retrives the file and reads all the words into word_list. It then goes through and stips
    #  the new line characters from the words. Afterwards it chooses a random word from the list, sets the length,
    #  retreives the number of attempts the player wants to play with (will probably alter at some point, read the
    #  respective funtion's description), initializes the shown_word variables to a series of "_"'s to mimic the
    #  original hangman, and finally calls the start game function.

    def __init__(self):
        with open("words.txt", "r") as f:
            self.word_list = f.readlines()
        i = 0
        while i < len(self.word_list)-1:
            self.word_list[i] = self.word_list[i][0:-2]
            i += 1
        self.word = random.choice(self.word_list)
        self.length = len(self.word)
        self.attempts = self.get_number_of_attempts()
        self.shown_word = self.initial_shown_word()
        self.start_game()

    #  This function initializes the 'shown_word' variables to all "_". It goes through a while loops that ends as soon
    #  as the length of the actual word has been reached. It adds one "_" for every letter in the 'word'.
    #  returns 'shown_word'

    def initial_shown_word(self):
        i = 0
        self.shown_word = []
        while i < len(self.word):
            self.shown_word.append("_")
            i += 1
        return self.shown_word

    #  This function shows the word just like it would in the original hagman. It starts with a string and then goes
    #  through and adds what is in the 'shown_word' variable and a space to the string to print out and show nice and
    #  cleanly.
    #  Returns 'print_string', or the string to print that shows the word cleanly.

    def show_word(self):
        i = 0
        print_string = ""
        while i < self.length-1:
            print_string += self.shown_word[i] + " "
            i += 1
        print_string += self.shown_word[i]
        return print_string

    #  This function shows the player the letters that are available to choose from in a clean way like the method
    #  above.
    #  Returns the same as above

    def show_letters_to_guess(self):
        i = 0
        print_string = ""
        while i < len(self.letters_to_guess)-1:
            print_string += self.letters_to_guess[i] + " "
            i += 1
        print_string += self.letters_to_guess[i]
        return print_string

    #  This function gets the number of attempts from the player. It first calls the ask_for_attempts function that
    #  does the actual asking. This function more or less does the error checking, for a string that can be cast as an
    #  int and for a number greater than 0.
    #  Returns 'attempts'

    def get_number_of_attempts(self):
        attempts = self.ask_for_attempts()
        try:
            attempts = int(attempts)
            while attempts < 1:
                print "Not enough lives entered. This is ridiculous. Asking again. \n"
                attempts = int(self.ask_for_attempts())
        except:
            print "Not an integer"
            self.get_number_of_attempts()
        return attempts

    #  This function does the actual asking for the attempts. Uses raw_input.
    #  Returns the input as a string.

    def ask_for_attempts(self):
        inpt = raw_input("How many lives would you like to start with? I suggest a number near ten. \n")
        return "" + inpt

    #  This function attempts to match the guessed letter with a letter(s) from the 'word'. It goes through a loops and
    #  if it should come across a match it sets the 'matched' variable to true, adds one to 'winning_letters', and calls
    #  the add_letter() method to add that letter to the shown_word variable.
    #  Returns 'matched'

    def match_letter(self, guess):
        i = 0
        matched = False
        while i < len(self.word):
            if guess == self.word[i]:
                self.winning_letters += 1
                matched = True
                self.add_letter(guess, i)
            i += 1
        return matched

    def add_letter(self, guess, index):
        # print "Self.shown_word:", len(self.shown_word), "Index:", index, "Guess:", guess
        self.shown_word[index] = guess

    def get_guess(self):
        guess = raw_input("What is your guess? \n").lower()
        if guess not in self.letters_to_guess:
            print "You either did not guess an actual letter (singular), or you guessed a letter " \
                  "you have already guessed \n"
            guess = self.get_guess().lower()
        if guess in self.letters_to_guess:
            return guess

    def start_game(self):
        while (self.attempts > 0) and (self.winning_letters < self.length):
            guess = self.get_guess()
            matched = self.match_letter(guess)
            if matched is False:
                self.take_letter_out(guess)
                self.wrong_guess()
            if matched is True:
                self.take_letter_out(guess)
                self.right_guess()
        self.ask_to_play_again()

    def ask_to_play_again(self):
        inputs = raw_input("Would you like to play again? \n")
        if inputs.lower() == "yes":
            self.new_game()

    def wrong_guess(self):
        self.attempts -= 1
        print "You guessed WRONG, you have", self.attempts, "lives left. Here is what you have.\n" \
            "This is what you can guess", self.show_letters_to_guess(), "\n\n", "This is what you have of the word so far", \
            self.show_word(), "\n\n"
        if self.attempts == 0:
            print "You lose, here is the word you were trying to guess", "\n", self.word

    def right_guess(self):
        if self.winning_letters == self.length:
            print self.show_word(), "\n", "You win! \n"
            self.win_condition = True
        else:
            print "CORRECT! Here is what you have so far. \n", self.show_word(), "\n\n", \
                "This is what you can guess", "\n", self.show_letters_to_guess(), "\n", "You have", self.attempts, \
                " lives left"

    def take_letter_out(self, guess):
        self.letters_to_guess.remove(guess)

    def new_game(self):
        self.word = random.choice(self.word_list)
        self.winning_letters = 0
        self.win_condition = False
        self.length = len(self.word)
        self.attempts = self.get_number_of_attempts()
        self.shown_word = self.initial_shown_word()
        self.letters_to_guess = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                 "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.start_game()

new_game = HangMan()



