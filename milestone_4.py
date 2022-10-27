import random


class Hangman():
    def __init__(self, word_list, num_lives=5) -> None:
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_" for ch in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess) -> None:
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for key, value in enumerate(self.word):
                if value == guess:
                    self.word_guessed[key] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)

    def ask_for_input(self) -> None:
        while (True):
            guess = input("Please enter a single letter: ")
            if (len(guess) != 1) or not (guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)


word_list = ["Apple", "Banana", "Pear", "Orange", "Strawberry"]
test_game = Hangman(word_list)
test_game.ask_for_input()
