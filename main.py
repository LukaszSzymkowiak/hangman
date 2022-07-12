from functions import *
from hangman_pics import *


def main():
    tries = 0
    lifes = 6
    random_word = random_word_func()
    used_letters = []
    hidden_word = hidden_word_func(random_word)
    while tries != lifes and hidden_word != random_word:
        print(f"Life {hangman_pics[tries]}\n"
              f"Used letters {used_letters}\n"
              f"Hidden word {hidden_word}\n")
        user_guess = input("Type a letter: \n")
        print()
        if user_guess in used_letters:
            print("Letter already used.\n")
        elif user_guess in random_word:
            new_hidden_word = ""
            for i in range(len(random_word)):
                if user_guess == random_word[i]:
                    new_hidden_word += user_guess
                else:
                    new_hidden_word += hidden_word[i]
            hidden_word = new_hidden_word
        else:
            used_letters.append(user_guess)
            tries += 1
    if hidden_word == random_word:
        print("\nCorrect!")
    else:
        print(f"Used letters: {used_letters}\n"
              f"Lost!!!\n"
              f"{hangman_pics[tries]}")


if __name__ == "__main__":
    main()
