# V Imports V
import random
import getpass

# V Variables etc V
secret_word = ""
guess_word = ""
guesses = 10
guess = ""
char_count = 0
ag_count = 0
IsAgain = False
ag_index = 0
words = ["angle", "ant", "apple", "arch", "arm", "army", "baby", "bag", "ball", "band", "basin", "basket", "bath", "bed", "bee", "bell", "berry", "bird", "blade", "board", "boat", "bone", "book", "boot", "bottle", "box", "boy", "brain", "brake", "branch", "brick", "bridge", "brush", "bucket", "bulb", "button", "cake", "camera", "card", "cart", "carriage", "cat", "chain", "cheese", "chest", "chin", "church", "circle", "clock", "cloud", "coat", "collar", "comb", "cord", "cow", "cup", "curtain", "cushion", "dog", "door", "drain", "drawer", "dress", "drop", "ear", "egg", "engine", "eye", "face", "farm", "feather", "finger", "fish", "flag", "floor", "fly", "foot", "fork", "fowl", "frame", "garden", "girl", "glove", "goat", "gun", "hair", "hammer", "hand", "hat", "head", "heart", "hook", "horn", "horse", "hospital", "house", "island", "jewel", "kettle", "key", "knee",
         "knife", "knot", "leaf", "leg", "library", "line", "lip", "lock", "map", "match", "monkey", "moon", "mouth", "muscle", "nail", "neck", "needle", "nerve", "net", "nose", "nut", "office", "orange", "oven", "parcel", "pen", "pencil", "picture", "pig", "pin", "pipe", "plane", "plate", "plough", "pocket", "pot", "potato", "prison", "pump", "rail", "rat", "receipt", "ring", "rod", "roof", "root", "sail", "school", "scissors", "screw", "seed", "sheep", "shelf", "ship", "shirt", "shoe", "skin", "skirt", "snake", "sock", "spade", "sponge", "spoon", "spring", "square", "stamp", "star", "station", "stem", "stick", "stocking", "stomach", "store", "street", "sun", "table", "tail", "thread", "throat", "thumb", "ticket", "toe", "tongue", "tooth", "town", "train", "tray", "tree", "trousers", "umbrella", "wall", "watch", "wheel", "whip", "whistle", "window", "wing", "wire", "worm"]
availible_guesses = "abcdefghijklmnopqrstuvwxiz"

# V Functions V


def Replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


# SPACER
# SPACER
# SPACER

print("""
Loaded Hangman.py | Picks a random word, user tries to guess it

Commands:
custom - set a custom secret word with a custom amount of guesses
""")

while True:
    print("Would you like to start the game? (yes/no)") if not IsAgain else print(
        "Would you like try again? (yes/no)")

    command = input("> ").lower().strip()

    if command == "yes":
        guesses = 10

        availible_guesses = "abcdefghijklmnopqrstuvwxiz"
        secret_word = random.choice(words)
        guess_word = "_" * len(secret_word)

        IsAgain = True

        print("")

        while guess_word != secret_word and guesses != 0:
            char_count = 0
            ag_count = 0
            guess_index = 0
            ag_index = 0

            if guess_word == secret_word:
                break

            print(f"You have {guesses} guesses left.")
            print(f"Letters: {availible_guesses}")
            print(f"Word: {guess_word}\n")

            guess = input("> ").lower().strip()

            guesses -= 1

            for char in availible_guesses:
                ag_index = availible_guesses.find(
                    guess, 0 + ag_count, 1 + ag_count)
                if ag_index >= 0:
                    availible_guesses = Replacer(
                        availible_guesses, " ", ag_index)
                ag_count += 1

            if guess == secret_word:
                break

            for char in secret_word:
                guess_index = secret_word.find(
                    guess, 0 + char_count, 1 + char_count)

                if guess_index >= 0:
                    ag_index = 0
                    ag_count = 0
                    guess_word = Replacer(guess_word, guess, guess_index)

                char_count += 1

        if guess_word == secret_word:
            print("You guessed the word, you win!")
            print(f"The word was {secret_word}.\n")

        elif guess == secret_word:
            print("You guessed the word, you win!")
            print(f"The word was {secret_word}.\n")

        elif guesses == 0:
            print("You ran out of guesses, you lose!")
            print(f"The word was {secret_word}.\n")

    elif command == "custom":

        availible_guesses = "abcdefghijklmnopqrstuvwxiz"

        print("What is the secret word? (eg. bread)")
        secret_word = getpass.getpass("> ")
        guess_word = "_" * len(secret_word)

        print("How manu guesses would you like? (eg. 10)")
        guesses = int(input("> "))

        IsAgain = True

        print("")

        while guess_word != secret_word and guesses != 0:
            char_count = 0
            ag_count = 0
            guess_index = 0
            ag_index = 0

            if guess_word == secret_word:
                break

            print(f"You have {guesses} guesses left.")
            print(f"Letters: {availible_guesses}")
            print(f"Word: {guess_word}\n")

            guess = input("> ").lower().strip()

            guesses -= 1

            for char in availible_guesses:
                ag_index = availible_guesses.find(
                    guess, 0 + ag_count, 1 + ag_count)
                if ag_index >= 0:
                    availible_guesses = Replacer(
                        availible_guesses, " ", ag_index)
                ag_count += 1

            if guess == secret_word:
                break

            for char in secret_word:
                guess_index = secret_word.find(
                    guess, 0 + char_count, 1 + char_count)

                if guess_index >= 0:
                    ag_index = 0
                    ag_count = 0
                    guess_word = Replacer(guess_word, guess, guess_index)

                char_count += 1

        if guess_word == secret_word:
            print("You guessed the word, you win!")
            print(f"The word was {secret_word}.\n")

        elif guess == secret_word:
            print("You guessed the word, you win!")
            print(f"The word was {secret_word}.\n")

        elif guesses == 0:
            print("You ran out of guesses, you lose!")
            print(f"The word was {secret_word}.\n")

    elif command == "no":
        break

print("Goodbye!")
