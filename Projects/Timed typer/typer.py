"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank

response = ""

def play_round(words, seconds):
    """Returns True if the user successfully completed the round."""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input("(" + str(seconds) + " seconds) " + words + "\n")
    stop = time.time()

    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    if not response == words:
        return 1
    # Player lost due to misspelled word.
    elif not within_time_limit:
        return 2
    # Player lost due to timeout.
    else:
        return 0
    # Player won.

def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words.""" 
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)

def get_score(level, round):
    """Returns the score based on difficulty."""
    if level <= 3:
        score = ((level - 1) * 12) + ((round - 1) * 3)
    elif level <= 6:
        score = ((level - 4) * 20) + ((round - 1) * 5) + 36
    else:
        score = ((level - 7) * 28) + ((round - 1) * 7) + 96

    return score

def get_high_score(score, high_score):
    """Returns the highest score."""
    if score > high_score:
        high_score = score

    return high_score

def is_high_score(score, high_score):
    """Returns True if the last score is the highest."""
    if score > high_score:
        return True
    else:
        return False
    
def player_progression(level, round):
    """Tracks player's victory status and game progression."""
    # Uses pick_random_words and play_round from typer.py.
    # Difficulty increases with later levels.
    if level == 1:                    
        words_to_type = pick_random_words(round, "easy")
        passed = play_round(words_to_type, 15)
    elif level == 2:
        words_to_type = pick_random_words(round, "easy")
        passed = play_round(words_to_type, 12)
    elif level == 3:
        words_to_type = pick_random_words(round, "easy")
        passed = play_round(words_to_type, 9)
    elif level == 4:
        words_to_type = pick_random_words(round, "medium")
        passed = play_round(words_to_type, 18)
    elif level == 5:
        words_to_type = pick_random_words(round, "medium")
        passed = play_round(words_to_type, 15)
    elif level == 6:
        words_to_type = pick_random_words(round, "medium")
        passed = play_round(words_to_type, 12)
    elif level == 7:
        words_to_type = pick_random_words(round, "hard")
        passed = play_round(words_to_type, 25)
    elif level == 8:
        words_to_type = pick_random_words(round, "hard")
        passed = play_round(words_to_type, 21)
    else:
        words_to_type = pick_random_words(round, "hard")
        passed = play_round(words_to_type, 18)

    return passed
