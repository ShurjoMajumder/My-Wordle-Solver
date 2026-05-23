import collections
import random
from pathlib import Path


debugging = False
NUM_GUESSES = 6


def valid_guess(guess: str, w_set: set[str]) -> bool:
    if len(guess) != 5:
        print("Invalid input")
        return False
    if guess not in w_set:
        print("Word is not in the word list")
        return False
    return True


def find_matches(guess: str, actual: str) -> str:
    squares = ['⬜'] * 5
    counts: dict[str, int] = dict(collections.Counter(actual))

    # Pass 1: greens
    for i, (g, a) in enumerate(zip(guess, actual)):
        if g == a:
            squares[i] = '🟩'
            counts[g] -= 1

    # Pass 2: yellows
    for i, g in enumerate(guess):
        if squares[i] == '⬜' and counts.get(g, 0) > 0:
            squares[i] = '🟨'
            counts[g] -= 1

    return ''.join(squares)


if __name__ == '__main__':
    with Path("./data/word_list.txt").open() as f:
        word_list: list[str] = f.read().split()
    if not word_list:
        print("Failed to load word list")
        exit(1)

    print("Guess the 5-letter word!")

    word_set = set(word_list)
    word = random.choice(word_list)
    if debugging:
        print(word)

    guesses = 0
    while guesses < NUM_GUESSES:
        input_guess = input()
        clean_guess = input_guess.upper()
        if not valid_guess(clean_guess, word_set):
            continue
        guesses += 1
        s = find_matches(clean_guess, word)
        print(s)
        if s == '🟩🟩🟩🟩🟩':
            break

    if guesses == 6:
        print(word)
    else:
        print(guesses)
