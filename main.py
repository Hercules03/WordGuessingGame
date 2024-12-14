import random

print("welcome to the word guessing game!")
print("The word is a 5 letter word.")
print("You will have 5 guesses to guess the word.")
print("Good luck!")

with open("word.txt", "r") as f:
    words = f.readlines()

processedWord = [word.rstrip("\n").lower() for word in words]

randomWord = random.choice(processedWord)

misplacedLetters = []
guessedWords = []

word = ["_", "_", "_", "_", "_"]

numberOfGuesses = 0

condition = "Loss"


while numberOfGuesses < 5:
    
    print(word)
    
    userGuess = input("Enter your guess: ").lower()
    
    if not(userGuess.isalpha()):
        print("Please enter a word!!")
        continue
    
    if len(userGuess) != 5:
        print("Please enter a word with 5 letters!!")
        continue
    
    if userGuess in guessedWords:
        print("You already guessed this word!!")
        continue
    
    for index, letter in enumerate(userGuess):
        if letter in randomWord:
            if letter not in word and index == randomWord.index(letter):
                word[index] = letter
                if letter in misplacedLetters:
                    misplacedLetters.remove(letter)
            else:
                if letter not in word:
                    misplacedLetters.append(letter)
                    print(f"'{letter}' appears in the word, but the position is wrong. Try again!")
            
    if word == list(randomWord):
        print(f"You got the word, {randomWord}!! Congrat!!")
        condition = "Win"
        break
    if userGuess != randomWord:
        guessedWords.append(userGuess)
            
    print(f"Missplaced letters: {set(misplacedLetters)}")
    print(f"Gussed words: {set(guessedWords)}")
    
    print("--------------------------------")
    
    numberOfGuesses += 1
    print(f"You have {5-numberOfGuesses} guesses left.")


if condition == "Loss":
    print("You lost the game!")