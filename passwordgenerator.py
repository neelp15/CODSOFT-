import random
import string

def password_generator():
    print("Welcome to the Password Generator!")
    
    try:
        # Prompt the user for password length
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            return

        # Character pools
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        # Combine all characters
        all_characters = lower_case + upper_case + digits + special_characters

        # Generate the password
        password = ''.join(random.choice(all_characters) for _ in range(length))

        # Display the generated password
        print(f"Your generated password is: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

# Run the password generator
password_generator()
