import secrets
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: You must include at least one character type.")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    if password:
        print("Your generated password is:", password)
    else:
        print("No characters selected. Password generation failed.")

if __name__ == "__main__":
    main()
