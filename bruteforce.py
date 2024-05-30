import hashlib

# Target hash
target_hash = "0395df69dee8a42152c3de07fb3d50f67547664a"

# Function to hash a password using SHA-1
def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

# Function to perform brute force attack
def brute_force_attack():
    # Define the character set
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Define the maximum password length to try
    max_length = 8

    # Loop through all possible password lengths
    for length in range(1, max_length + 1):
        # Generate all possible passwords of the given length
        for password in generate_passwords(charset, length):
            # Hash the password
            hashed_password = hash_password(password)
            
            # Check if the hashed password matches the target hash
            if hashed_password == target_hash:
                return password  # Password found

    return None  # Password not found

# Function to generate all possible passwords of a given length
def generate_passwords(charset, length):
    if length == 0:
        yield ""
    else:
        for char in charset:
            for password in generate_passwords(charset, length - 1):
                yield char + password

# Perform the brute force attack
password = brute_force_attack()

# Print the result
if password:
    print("Password found:", password)
else:
    print("Password not found")
