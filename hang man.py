#Purpose: Hangman game
#Author: Ken Vu
#Date:March 15th,2024
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#list of word
import random
words = ["pizza","burger","hotdog","bacon"]
#random choice of words
word = random.choice(words)
guess_words = ["_"]*len(word)
guessed_letters = set()
wrong_guesses = 0
max_wrong_guesses = 7
print(HANGMANPICS[0])
#Hangman
while wrong_guesses < max_wrong_guesses and "_" in guess_words:
    print(" ".join(guess_words))
    guess = input("Enter a letter: ").lower()
    if guess in word:        
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guess_words[i]= guess
    elif guess not in word:
            print("Wrong guess!")
            print(HANGMANPICS[1+wrong_guesses])
            wrong_guesses += 1
if '_' not in guess_words:
        print("Congratulations! You guessed the word:", word)
else:
        print("Sorry, you ran out of guesses. The word was:", word)

