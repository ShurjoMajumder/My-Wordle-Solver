import random
from pathlib import Path


def find_matches(guess: str, actual: str, actual_counts: dict[str, int]):
    squares: list[str] = ['⬜','⬜','⬜','⬜','⬜']

    guess_counts: dict[str, int] = {}

    for iga in enumerate(zip(guess, actual)):
        i, (g, a) = iga
        guess_counts[g] = guess_counts.get(g, 0) + 1

        if g not in actual:
            continue
        if guess_counts[g] <= actual_counts.get(g, 0):
            squares[i] = '🟨'
        if g == a:
            squares[i] = '🟩'

    return ''.join(squares)

if __name__ == '__main__':
    with Path("./data/word_list.txt").open() as f:
        word_list: list[str] = f.read().split(' ')
    if not word_list:
        print("Failed to load word list")

    print("Guess the 5-letter word!")

    word_set = set(word_list)
    word = random.choice(word_list)
    letter_counts = {}
    for letter in word:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    print(word)
    guesses = 0
    while guesses < 6:
        input_guess = input()
        clean_guess = input_guess.upper()

        if len(clean_guess) != 5:
            print("Invalid input")
            continue
        if clean_guess not in word_set:
            print("Word is not in the word list")
            continue

        guesses += 1
        s = find_matches(clean_guess, word, letter_counts)
        print(s)
        if s == '🟩🟩🟩🟩🟩':
            break

    if guesses == 6:
        print(word)
    else:
        print(guesses)
