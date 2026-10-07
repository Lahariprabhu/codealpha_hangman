import random
words = ["python", "computer", "programming", "keyboard", "developer"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = []
max_wrong_guesses = 6
print("   WELCOME TO HANGMAN")
print("x" * 30)
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses available.")
print()
while len(wrong_guesses) < max_wrong_guesses:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print("Wrong guesses:", len(wrong_guesses), "/", max_wrong_guesses)

    if wrong_guesses:
        print("Incorrect letters:", ", ".join(wrong_guesses))

    
    if all(letter in guessed_letters for letter in word):
        print()
        print("🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        print()
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter. Try another one.")
        print()
        continue

    if guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        wrong_guesses.append(guess)
        print("Wrong guess!")

    print()

else:
    print()
    print("Game Over!")
    print("You used all 6 incorrect guesses.")
    print("The word was:", word)

print()
print("=" * 40)
print("          THANK YOU FOR PLAYING!")
print("=" * 40)