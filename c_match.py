import random

COLORS = ["R", "G", "B", "W", "O"]
ATTEMPTS = 10
CODE_LENGTH = 4


def generate_code():
    """Generate a random secret code."""
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


def guess_code():
    """Ask the player to guess until a valid input is given."""
    while True:
        guess = input("Enter your guess (e.g. R G B O): ").upper().split()

        # Check length
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        # Check if all colors are valid
        invalid_colors = [color for color in guess if color not in COLORS]
        if invalid_colors:
            print(
                f"Invalid colors: {', '.join(invalid_colors)}. Valid colors: {', '.join(COLORS)}")
            continue

        # ✅ Valid guess
        return guess


def check_code(guess, real_code):
    """Check guess against the actual code and return result."""
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count occurrences of each color in the code
    for color in real_code:
        color_counts[color] = color_counts.get(color, 0) + 1

    # First pass: check correct positions
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            color_counts[guess[i]] -= 1  # consume one occurrence

    # Second pass: check correct color but wrong position
    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i] and color_counts.get(guess[i], 0) > 0:
            incorrect_pos += 1
            color_counts[guess[i]] -= 1  # consume one occurrence

    return correct_pos, incorrect_pos


def game():
    print(
        f"🎯 Welcome to Mastermind! You have {ATTEMPTS} attempts to guess the code.")
    print("The valid colors are:", *COLORS)

    code = generate_code()

    # 👇 show the answer right away
    print("👉 (DEBUG) The secret code is:", *code)

    for attempt in range(1, ATTEMPTS + 1):
        print(f"\nAttempt {attempt}/{ATTEMPTS}")
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(
                f"🎉 You guessed the code in {attempt} tries! The code was:", *code)
            break

        print(
            f"✅ Correct Positions: {correct_pos} | 🎨 Correct Colors (Wrong Position): {incorrect_pos}")

    else:
        print("❌ You ran out of attempts. The code was:", *code)


if __name__ == "__main__":
    game()
