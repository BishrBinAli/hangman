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
