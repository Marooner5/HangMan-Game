import random


class HangMan:

    word = ""
    length = 0
    attempts = 0
    win_condition = False
    winning_letters = 0
    letters_to_guess = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
    shown_word = []
    game_start = 0
    word_list = []

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

    def initial_shown_word(self):
        i = 0
        while i < len(self.word):
            self.shown_word.append("_")
            i += 1
        return self.shown_word

    def get_number_of_attempts(self):
        try:
            attempts = int(self.ask_for_attempts())
            while attempts < 1:
                print "Not enough attempts entered. This is ridiculous. Asking again. \n"
                attempts = int(self.ask_for_attempts())
        except:
            print "Not an integer"
            self.get_number_of_attempts()
        return attempts

    @staticmethod
    def ask_for_attempts():
        inpt = raw_input("How many attempts would you like to start with? I suggest a number near ten. \n")
        return "" + inpt

    def match_letter(self, guess):
        # go through a loop to see how many letters match the guess and make changes accordingly.
        # have a variable that holds the indexes at which the letters were found.
        # what needs to happen if a letter matches
        #   add 1 to winning_letters each time there's a match
        #   hold the index at which the letter was found each time
        #   take that letter away from the letters available to guess from
        # what needs to happen if a letter doesn't match at all
        #   if a letter is not found at all or string.find(guess) == -1 then
        #       add one to attempts and take that letter away from the available letters to guess from
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
        guess = raw_input("What is your guess? \n")
        if guess not in self.letters_to_guess:
            print "You either did not guess an actual letter (singular), or you guessed a letter " \
                  "you have already guessed"
            self.get_guess()
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
        input = raw_input("Would you like to play again? \n")
        if input.lower() == "yes":
            self.new_game()

    def wrong_guess(self):
        self.attempts -= 1
        print "You guessed WRONG, you have", self.attempts, "attempts left. Here is what you have.\n " \
            "This is what you can guess", self.letters_to_guess, "\n\n", "This is what you have of the word so far", \
            self.shown_word, "\n\n"
        if self.attempts == 0:
            print "You lose"

    def right_guess(self):
        if self.winning_letters == self.length:
            print self.shown_word, "\n", "You win! \n"
            self.win_condition = True
        else:
            print "Checking if you won because you guessed RIGHT. So here is what you have so far. \n", self.shown_word,\
                "\n\n", "This is what you can guess", "\n", self.letters_to_guess, "\n"

    def take_letter_out(self, guess):
        self.letters_to_guess.remove(guess)

    def new_game(self):
        self.word = random.choice(self.word_list)
        self.game_start = 0
        self.winning_letters = 0
        self.win_condition = False
        self.length = len(self.word)
        self.attempts = self.get_number_of_attempts()
        self.shown_word = self.initial_shown_word()
        self.letters_to_guess = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                 "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.start_game()

new_game = HangMan()



