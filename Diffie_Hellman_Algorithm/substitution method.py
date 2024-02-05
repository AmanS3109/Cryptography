def calculate_key(p, g, private_key):
    """Calculates the public key using Diffie-Hellman algorithm."""
    return (g ** private_key) % p


def encrypt(message, shared_secret):
    """Encrypts a message using a simple shift cipher."""
    encrypted_message = ''.join(
        chr((ord(char) + shared_secret) % 256) for char in message
    )
    return encrypted_message


def decrypt(encrypted_message, shared_secret):
    """Decrypts a message using the same shift cipher."""
    decrypted_message = ''.join(
        chr((ord(char) - shared_secret) % 256) for char in encrypted_message
    )
    return decrypted_message


if __name__ == "__main__":
    try:
        p = int(input("Enter a prime number (p): "))
        g = int(input("Enter a primitive root modulo p (g): "))

        private_key_sender = int(input("Enter Sender's private key: "))
        private_key_receiver = int(input("Enter Receiver's private key: "))

        public_key_sender = calculate_key(p, g, private_key_sender)
        public_key_receiver = calculate_key(p, g, private_key_receiver)

        shared_secret_sender = calculate_key(p, public_key_receiver, private_key_sender)
        shared_secret_receiver = calculate_key(p, public_key_sender, private_key_receiver)

        message = input("Enter the message to be encrypted: ")

        encrypted_message = encrypt(message, shared_secret_sender)
        decrypted_message = decrypt(encrypted_message, shared_secret_receiver)

        print(f"Sender's public key: {public_key_sender}")
        print(f"Receiver's public key: {public_key_receiver}")
        print(f"Shared secret for Sender: {shared_secret_sender}")
        print(f"Shared secret for Receiver: {shared_secret_receiver}")
        print(f"Original Message: {message}")
        print(f"Encrypted Message: {encrypted_message}")
        print(f"Decrypted Message: {decrypted_message}")

    except ValueError as e:
        print(f"Error: Invalid input. Please enter valid integers.")