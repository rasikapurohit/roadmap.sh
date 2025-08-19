import random

DIFFICULTY_LEVELS = {
    1: {"chances": 10, "label": "Easy"},
    2: {"chances": 5, "label": "Medium"},
    3: {"chances": 3, "label": "Hard"},
}

def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        user_input = input(prompt).strip()
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        value = int(user_input)
        if min_val is not None and value < min_val:
            print(f"Please enter a number >= {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"Please enter a number <= {max_val}.")
            continue

        return value

def main():
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice:
""")

    # Choose difficulty
    for key, level in DIFFICULTY_LEVELS.items():
        print(f"{key}. {level['label']} ({level['chances']} chances)")

    choice = get_valid_int("Enter your choice: ", 1, 3)
    difficulty = DIFFICULTY_LEVELS[choice]

    # Game setup
    computer_guess = random.randint(1, 100)
    attempts_left = difficulty["chances"]
    attempt_count = 0

    print(f"\nGreat! You have selected {difficulty['label']} level.")
    # print(f"You have {attempts_left} chances. Let's begin!")

    # Guessing loop
    while attempts_left > 0:
        guess = get_valid_int("\nEnter your guess (1-100): ", 1, 100)
        attempt_count += 1
        attempts_left -= 1

        if guess == computer_guess:
            print(f"Congratulations! You guessed it in {attempt_count} attempts.")
            break
        elif guess < computer_guess:
            print("The number is greater than", guess)
        else:
            print("The number is less than", guess)

        # print(f"Chances left: {attempts_left}")

    else:
        print(f"Game over! The correct number was {computer_guess}.")

if __name__ == "__main__":
    main()


# import random
#
# easy_guesses = 10
# medium_guesses = 5
# hard_guesses = 3
#
# computer_guess = random.randint(1, 100)
#
# guess_choice = int(input("""Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# You have 5 chances to guess the correct number.
#
# Please select the difficulty level:
# 1. Easy (10 chances)
# 2. Medium (5 chances)
# 3. Hard (3 chances)
#
# Enter your choice:
# """))
#
# if guess_choice > 3:
#     print("Invalid level selected, try again.")
#     guess_choice = int(input("""Please select the difficulty level:
# 1. Easy (10 chances)
# 2. Medium (5 chances)
# 3. Hard (3 chances)
#
# Enter your choice:"""))
#
# guess_level_map = {
#     1: {'g': easy_guesses, 'label': 'Easy'},
#     2: {'g': medium_guesses, 'label': 'Medium'},
#     3: {'g': hard_guesses, 'label': 'Hard'},
# }
#
# user_guess = int(input (f"""Great! You have selected the {guess_level_map[guess_choice]['label']} difficulty level.
# Let's start the game!
#
# Enter your guess:
# """))
#
# user_attempts = []
# while guess_level_map[guess_choice]['g'] != 0:
#     user_attempts.append(user_guess)
#     guess_level_map[guess_choice]['g'] -= 1
#     if user_guess == computer_guess:
#         print("Congratulations! You guessed the correct number in ",len(user_attempts)  ," attempts.")
#         exit()
#     elif user_guess < computer_guess:
#         print("Incorrect! The number is greater than ", user_guess)
#         user_guess = int(input("Enter your guess: "))
#     elif user_guess > computer_guess:
#         print("Incorrect! The number is less than ", user_guess)
#         user_guess = int(input("Enter your guess: "))