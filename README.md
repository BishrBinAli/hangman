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
