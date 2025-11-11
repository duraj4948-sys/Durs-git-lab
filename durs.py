"""
======================================================
Durs Password Generator v0.1
Author: Joshua Dura
Date: 2025-11-05
Description:
     Gibuhat ko kini nga password generator aron makatabang sa
     paghimo ug luwas ug ma-customize nga mga password.
     Adunay kini dynamic nga pag-sukod sa kalig-on sa password.
======================================================
"""

import random
import string
import time


def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """Generates a secure random password based on user preferences."""
    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return " No character sets selected."

    return ''.join(random.choice(chars) for _ in range(length))


def password_strength(length):
    """Evaluates password strength based on length."""
    if length < 8:
        return " WEAK"
    elif length < 12:
        return " MEDIUM"
    else:
        return " STRONG"


def main():
    """Main execution flow of the password generator."""
    print("═" * 52)
    print(" Welcome to Durs Password Generator v0.1")
    print("═" * 52)

    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_letters = input("Include letters? (y/n): ").lower() == "y"
        use_numbers = input("Include numbers? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"

        print("\n Generating secure password...")
        time.sleep(1)

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\n Generated Password:", password)
        print("Strength:", password_strength(length))

        print("\n© 2025 Durs-git-lab | Terminal Edition")
        print("Thank you for using a Durs-git-lab innovation")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
