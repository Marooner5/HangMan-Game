import random


class HangMan:

    word = ""
    length = 0
    attempts = 0
    win_condition = False
    winning_letters = 0
    letters_to_guess = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
    shown_word = ""

    def __init__(self):
        with open("words.txt", "r") as f:
            word_list = f.readlines()
        i = 0
        while i < len(word_list)-1:
            word_list[i] = word_list[i][0:-2]
            i += 1
        self.word = random.choice(word_list)
        self.length = len(self.word)
        self.attempts = self.get_number_of_attempts()
        self.start_game()

    def print_spaces(self):
        for letter in self.word:
            self.shown_word += "_"
        print self.shown_word  # need to store this as a list

    def get_number_of_attempts(self):
        try:
            attempts = int(self.ask_for_attempts())
            return attempts
        except:
            print "Not an integer"
            self.get_number_of_attempts()

    @staticmethod
    def ask_for_attempts():
        inpt = raw_input("How many attempts would you like to start with? I suggest a number near ten. \n")
        return "" + inpt

    def match_letter(self):
        pass
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
        guess = self.get_guess()
        while i < len(self.word):
            if guess == self.word[i]:
                self.winning_letters += 1
                matched = True
                self.add_letter(guess, i)
        return matched

    def add_letter(self, guess, index):
        self.shown_word[index] = guess

    def get_guess(self):
        guess = raw_input("What is your guess?")
        if guess not in self.letters_to_guess:
            print "You either did not guess an actual letter (singular), or you guessed a letter" \
                  "you have already guessed"
        if guess in self.letters_to_guess:
            return guess

    def start_game(self):
        while self.attempts > 1 or self.win_condition is False:
            if self.match_letter() is False:
                self.wrong_guess()
            if self.match_letter() is True:
                print "You guess right, here is what you have."
                print self.shown_word, self.letters_to_guess

    def wrong_guess(self):
        self.attempts -= 1
        print self.attempts, "This are your attempts. You guess wrong, here is what you have."
        print self.letters_to_guess, self.shown_word

new_game = HangMan()


