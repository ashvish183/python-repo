# Created and Ran using Python IDLE
import random

print("Welcome to Hangman")
difficulty = input("Select a difficulty: easy, medium, hard\n")

while difficulty not in ["easy", "medium", "hard"]:
	difficulty = input("invalid difficulty, select easy, medium, or hard\n")

print(f"selecting a {difficulty} word...")

# open words.txt, save all words to data structure

# map easy medium and hard to word length and turns
all_words = list(set(open("words.txt", "r").read().split()))
filtered_words = []

if difficulty == "easy":
	turns = 20
	for word in all_words:
		if len(word) < 5:
			filtered_words.append(word)

if difficulty == "medium":
	turns = 15
	for word in all_words:
		if len(word) >= 5 and len(word) < 7:
			filtered_words.append(word)

if difficulty == "hard":
	turns = 10
	for word in all_words:
		if len(word) >= 7:
			filtered_words.append(word)
secret_word = random.choice(filtered_words)
guesses = ''

# game loop

while turns > 0:
     
    failed = 0
     
    for char in secret_word: 
         
        if char in guesses: 
            print(char, end=" ")
             
        else: 
            print("_", end=" ")
             
            failed += 1
             
    print()
    if failed == 0:
        print("You Win") 
         
        print("The word is: ", secret_word) 
        break
     
    guess = input("guess a character: ")

    if guess in guesses: 
        print(f"You already guessed '{guess}'")

    elif guess not in secret_word:
        turns -= 1
         
        print("Wrong")
         
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("The word was: ", secret_word) 
            print("You Lose")

    
    guesses += guess 
