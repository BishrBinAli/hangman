# Hangman

Project to implement the hangman game

## Milestone 2

Implemented the following:

- Create list of possible words
- Select a word from the list at random
- Accept user input and check if its a single character and an alphabet

```python
word_list = ["Apple", "Banana", "Pear", "Orange", "Strawberry"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")

if (len(guess) == 1) and (guess.isalpha()):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 3

Implemented the following:

- Iteratively check till user enters a valid input
- Check if user guess is in the word
- Create functions to run the checks

check_guess() function takes the guessed letter as an argument, converts it into lower case and checks if it is present in the word or not

```python
def check_guess(guess):
guess = guess.lower()
if (guess in word):
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
```

ask_for_input() function iteratively asks the user to enter their guess until a valid guess is given. Then, it checks if the guess is present in the word by calling the check_guess() function

```python
def ask_for_input():
    while (True):
        guess = input("Please enter a single letter: ")

        if (len(guess) == 1) and (guess.isalpha()):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)
```

## Milestone 4

Implemented the following:

- Create a class to represent the game
- Create methods to run the checks

Class Hangman() takes the possible word list and number of lives when creating an object and initialises the class attributes which are needed to run the game. It has two methods: check_guess() and ask_for_input(). The ask_for_input() method asks the user to enter a guess and checks if it is a valid guess and if it is, calls the check_guess() method to check if the guess is in the word or not.

```python
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
```
