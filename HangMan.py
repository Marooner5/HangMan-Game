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
#               source as soon as I find it. This is a class variable to make it easier for initiating a new game. It
#               also saves on time (even though its negligible).

# Above each method you will find a description of what it does. All methods are private as the only method we want
# to be able to be called from the outside is the __init__ method.


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

    #  What this does is it retrieves the file and reads all the words into word_list. It then goes through and strips
    #  the new line characters from the words. Afterwards it makes a call to the 'new_game()' method.

    def __init__(self):
        with open("words.txt", "r") as f:
            self.word_list = f.readlines()
        i = 0
        while i < len(self.word_list)-1:
            self.word_list[i] = self.word_list[i][0:-2]
            i += 1
        self.__new_game()

    #  This method initializes the 'shown_word' variables to all "_". It goes through a while loops that ends as soon
    #  as the length of the actual word has been reached. It adds one "_" for every letter in the 'word'.
    #  returns 'shown_word'

    def __initial_shown_word(self):
        i = 0
        self.shown_word = []
        while i < len(self.word):
            self.shown_word.append("_")
            i += 1
        return self.shown_word

    #  This method shows the word just like it would in the original hangman. It starts with a string and then goes
    #  through and adds what is in the 'shown_word' variable and a space to the string to print out and show nice and
    #  cleanly.
    #  Returns 'print_string', or the string to print that shows the word cleanly.

    def __show_word(self):
        i = 0
        print_string = ""
        while i < self.length-1:
            print_string += self.shown_word[i] + " "
            i += 1
        print_string += self.shown_word[i]
        return print_string

    #  This method shows the player the letters that are available to choose from in a clean way like the method
    #  above.
    #  Returns the same as above

    def __show_letters_to_guess(self):
        i = 0
        print_string = ""
        while i < len(self.letters_to_guess)-1:
            print_string += self.letters_to_guess[i] + " "
            i += 1
        print_string += self.letters_to_guess[i]
        return print_string

    #  This method gets the number of attempts from the player. It first calls the ask_for_attempts method that
    #  does the actual asking. This method more or less does the error checking, for a string that can be cast as an
    #  int and for a number greater than 0.
    #  Returns 'attempts'

    def __get_number_of_attempts(self):
        attempts = self.__ask_for_attempts()
        try:
            attempts = int(attempts)
            while attempts < 1:
                print "Not enough lives entered. This is ridiculous. Asking again. \n"
                attempts = int(self.__ask_for_attempts())
        except TypeError:
            print "Not an integer"
            self.__get_number_of_attempts()
        return attempts

    #  This method does the actual asking for the attempts. Uses raw_input.
    #  Returns the input as a string.

    def __ask_for_attempts(self):
        inputs = raw_input("How many lives would you like to start with? I suggest a number near ten. \n")
        return "" + inputs

    #  This method attempts to match the guessed letter with a letter(s) from the 'word'. It goes through a loops and
    #  if it should come across a match it sets the 'matched' variable to true, adds one to 'winning_letters', and calls
    #  the add_letter() method to add that letter to the shown_word variable.
    #  Returns 'matched'

    def __match_letter(self, guess):
        i = 0
        matched = False
        while i < len(self.word):
            if guess == self.word[i]:
                self.winning_letters += 1
                matched = True
                self.__add_letter(guess, i)
            i += 1
        return matched

    #  This method adds a letter to the 'shown_word' variable. Called after a successful guess.

    def __add_letter(self, guess, index):
        self.shown_word[index] = guess

    #  This method retrieves a guess from a user. It checks to see if it is in the guessable letters. If not its
    #  keeps asking.
    #  Returns the guess

    def __get_guess(self):
        guess = raw_input("What is your guess? \n").lower()
        if guess not in self.letters_to_guess:
            print "You either did not guess an actual letter (singular), or you guessed a letter " \
                  "you have already guessed \n"
            guess = self.__get_guess().lower()
        if guess in self.letters_to_guess:
            return guess

    #  This is the method that runs the game. It runs until the player either loses (self.attempts = 0) or wins
    #  self.winning_letters < self.length.  It calls the 'get_guess()' method and then makes other calls to see if the
    #  guess matched. If so it will call the 'right_guess()' method. If not: the 'wrong_guess()' method. Either way
    #  it will take that guess out of the list of letters that are available to guess.
    #  Does not return anything. If the loops ends it asks if the user wants to play again.

    def __start_game(self):
        while (self.attempts > 0) and (self.win_condition is False):
            guess = self.__get_guess()
            matched = self.__match_letter(guess)
            if matched is False:
                self.__take_letter_out(guess)
                self.__wrong_guess()
            if matched is True:
                self.__take_letter_out(guess)
                self.__right_guess()
        self.__ask_to_play_again()

    #  This method simply asks if the user would like to play again. Will probably need to make this more intuitive
    #  rather than looking for a simple "yes".
    #  Does not return anything. If the input is "yes" a new game will be started with 'new_game()'.

    def __ask_to_play_again(self):
        inputs = raw_input("Would you like to play again? \n")
        if inputs.lower() == "yes":
            self.__new_game()

    #  This method does all the necessary steps after a wrong guess is made. It takes one away from 'self.attempts'
    #  after which it prints out all the necessary info: how many lives you have left, what you can guess, what you
    #  currently have. If this makes 'self.attempts' 0 it will print out the word you were trying to guess and that you
    #  lose.
    #  Does not return anything.

    def __wrong_guess(self):
        self.attempts -= 1
        print "You guessed WRONG, you have", self.attempts, "lives left. Here is what you have.\n" \
            "This is what you can guess", self.__show_letters_to_guess(), "\n\n", "This is what you have of the word so far", \
            self.__show_word(), "\n\n"
        if self.attempts == 0:
            print "You lose, here is the word you were trying to guess", "\n", self.word

    #  This method does all the necessary steps after a right guess is made. Checks to see if the player has won. If so
    #  it prints a winning statement. If not, it shows that the player
    #  has guessed correctly and displays the necessary info for the player.
    #  Does not return anything.

    def __right_guess(self):
        if self.winning_letters == self.length:
            print self.__show_word(), "\n", "You win! \n"
            self.win_condition = True
        else:
            print "CORRECT! Here is what you have so far. \n", self.__show_word(), "\n\n", \
                "This is what you can guess", "\n", self.__show_letters_to_guess(), "\n", "You have", self.attempts, \
                " lives left"

    #  This method simply takes the guess out of the letters that the player sees that they can guess from.

    def __take_letter_out(self, guess):
        self.letters_to_guess.remove(guess)

    #  This method initiates a new game. It sets all of the necessary variables to their default values.

    def __new_game(self):
        self.word = random.choice(self.word_list)
        self.winning_letters = 0
        self.win_condition = False
        self.length = len(self.word)
        self.attempts = self.__get_number_of_attempts()
        self.shown_word = self.__initial_shown_word()
        self.letters_to_guess = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                 "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.__start_game()

new_game = HangMan()



