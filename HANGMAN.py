import random
import time
import sys

# Initial Steps to invite in the game:
print("\nWELCOME TO HANGMAN\n")
name = input("Enter your name: ")
print("\nHello " + name + "! Best of Luck!")
time.sleep(2)
print("\nThe game is about to start!\nLet's play HANGMAN!\n")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    
# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = YES, n = NO \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = YES, n = NO \n")
    if play_game == "y" or play_game == "Y":
        main()
        hangman()
    elif play_game == "n" or play_game == "N":
        print("\nTHANKS FOR PLAYING!! WE EXPECT YOU BACK AGAIN")
        sys.exit()
        
# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("\nThis is the Hangman Word: " + display + "\nEnter your guess: ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:             
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Already guessed! Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Oops Wrong guess. " + str(limit - count) + " \n guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Oops Wrong guess. " + str(limit - count) + "\n guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     O \n"
                 "  |     |\n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Oops Wrong guess. " + str(limit - count) + " \n guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Oops Wrong guess. " + str(limit - count) + " \n last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Oops Wrong guess. You are HANGED !!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("CONGRATULATIONS! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()
