import random
import string


def generate_password(length=8):
    # Combine lowercase, uppercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation  
    # Randomly select characters from the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Example usage
if __name__ == "__main__":
    password=generate_password(8)
    print("Generated Password:", password)

#Make  one password using the deafault length,and one with a custom length(12)
p1 = generate_password()
p2 = generate_password(12)

# print password details
print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))