#Purpose: Hangman game
#Author: Ken Vu
#Date:March 15th,2024
print("This 2 players Hangman game!!!!")
word = input("Can you choose one word ? ")
print("Player 1 choose: "+word)
print("************************************")
for i in range(70):
    print("                                                                  ")
#Convert the letter to "_"
guess_words = ["_"]*len(word)
guessed_letters = set()
#Number of chances
wrong_guesses = 0
max_wrong_guesses = 6
#**************************************************
print("Player 2 have "+str(max_wrong_guesses), " chances to guess the word")
print("**************************************")
#Drawing a hangman
hangman_parts = ["", "O"," | ",' / ','/|)',"(",')']
def drawing_hangman(wrong_guesses, hangman_parts):
    print(hangman_parts[wrong_guesses])    
    return wrong_guesses
#Main program
def hangman(wrong_guesses,hangman_parts):
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
                wrong_guesses += 1
                drawing_hangman(wrong_guesses,hangman_parts)
    if '_' not in guess_words:
            print("Congratulations! You guessed the word:", word)
    else:
            print("Sorry, you ran out of guesses. The word was:", word)
            print('''
              +---+
              O   |
             /|)  |
             ( )  |
                  |
                  |
            =========''')
hangman(wrong_guesses,hangman_parts)