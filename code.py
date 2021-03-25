#!/usr/bin/env python3

from __future__ import annotations

import random
import time

from typing import List

def setup_game() -> List[int]:
    """
    Print a time-delayed set of instructions for this game and return 3 randomly]
    generated numbers from 1 to 10 (inclusive).
    """
    instructions = [
        "1. The Computer will select 3 numbers from 1 to 10, you must guess all 3 numbers in the right order.",
        "2. Each time you guess, the computer will tell you how much numbers did you guess right, and tell you if those numbers were in the correct order.",
        "3. There is no limit to how much guesses you can use.",
        "4. You win by guessing all the correct numbers in the right order"
    ]

    print('=' * 60)

    for line in instructions:
        print(line)
        time.sleep(1)

    print('=' * 60)

    return random.choices(range(1, 11), k=3)

def check_number(unknown: int) -> bool:
    """
    Takes a random (to the user unknown) number as function parameter. The user
    is prompted to enter a guess. If the user guesses correctly return True, else
    return False.
    """
    guess = int(input(">>> "))

    if guess > unknown:
        print("You guessed too high!")
        return False
    elif guess < unknown:
        print("You guessed to low!")
        return False
    else:
        print("Your guess was correct!")
        return True

def start_game():
    """
    The main function of this game. For each number in nums_to_guess the user
    enters a number. The result of this comparison goes in guess_results.
    """
    guess_results = []
    nums_to_guess = setup_game()
    
    for num in nums_to_guess:
        guess_results.append(check_number(num))

    print("\nYou won!") if all(guess_results) else print("\nYou lost!")

# this section defines the entry point of your application
if __name__ == '__main__':
    start_game()
