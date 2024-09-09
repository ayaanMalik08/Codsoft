import random
import string

# Function to generate a random password
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Define possible characters for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has a mix of character types
    all_characters = lower + upper + digits + special
    
    # Guarantee at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the remaining password length with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle to ensure randomness
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

# Main function to run the password generator
def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            # Prompt the user to enter the desired password length
            length = int(input("Enter the desired password length (minimum 4): "))
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated Password: {password}")
            
            # Ask if the user wants to generate another password
            choice = input("\nDo you want to generate another password? (yes/no): ").lower()
            if choice != "yes":
                print("Thank you for using the Password Generator. Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
