import string
import random
import re

def check_password_strength(password):
    """Analyzes a password string and evaluates its strength based on specific criteria."""
    # Initialize checklist flags
    has_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    # Basic Regular Expression to look for at least one special character
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Calculate overall score based on met criteria
    criteria_met = sum([has_length, has_digit, has_upper, has_lower, has_special])

    print("\n--- Strength Analysis ---")
    print(f"[-] Length (8+ chars):   {'✓' if has_length else '✗'}")
    print(f"[-] Contains Digits:     {'✓' if has_digit else '✗'}")
    print(f"[-] Uppercase Letters:   {'✓' if has_upper else '✗'}")
    print(f"[-] Lowercase Letters:   {'✓' if has_lower else '✗'}")
    print(f"[-] Special Characters:  {'✓' if has_special else '✗'}")

    # Determine final evaluation tier
    if criteria_met == 5:
        return "STRONG"
    elif criteria_met >= 3:
        return "MEDIUM"
    else:
        return "WEAK"

def generate_strong_password(length=12):
    """Generates a secure, randomized password meeting all strength requirements."""
    if length < 8:
        print("[Warning] Overriding length to 8 to maintain minimum strength standard.")
        length = 8

    # Define standard character pools using the string module
    lower_pool = string.ascii_lowercase
    upper_pool = string.ascii_uppercase
    digit_pool = string.digits
    special_pool = "!@#$%^&*()"
    
    # Combined pool for remaining characters
    all_characters = lower_pool + upper_pool + digit_pool + special_pool

    # Step 1: Ensure at least one character from each required category exists
    password_chars = [
        random.choice(lower_pool),
        random.choice(upper_pool),
        random.choice(digit_pool),
        random.choice(special_pool)
    ]

    # Step 2: Fill the rest of the password length randomly from the combined pool
    for _ in range(length - 4):
        password_chars.append(random.choice(all_characters))

    # Step 3: Shuffle the list array randomly so categories don't appear in a fixed order
    random.shuffle(password_chars)

    # Convert character array list back into a single string chain
    return "".join(password_chars)

def main():
    """Main application loop managing console menu workflows."""
    while True:
        print("\n====== PASSWORD TOOLKIT ======")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")
        print("==============================")
        
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            user_pwd = input("Enter password to evaluate: ")
            if not user_pwd:
                print("[Error] Password input cannot be empty.")
                continue
            
            result = check_password_strength(user_pwd)
            print(f"\n>> Final Strength Assessment: **{result}** <<")

        elif choice == '2':
            try:
                length_input = input("Enter desired password length (Press Enter for default 12): ").strip()
                pwd_length = int(length_input) if length_input else 12
                
                generated_pwd = generate_strong_password(pwd_length)
                print("\n--- Generated Password ---")
                print(f"Password: {generated_pwd}")
                
                # Instant validation proofing loop
                strength_proof = check_password_strength(generated_pwd)
                print(f">> Verification Check: {strength_proof} <<")
            except ValueError:
                print("[Error] Invalid input. Please enter a valid number for length.")

        elif choice == '3':
            print("\nThank you for using the Password Toolkit. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice! Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
