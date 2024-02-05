def is_prime(num):
   """Efficiently checks if a number is prime."""
   if num < 2:
       return False
   for i in range(2, int(num**0.5) + 1):
       if num % i == 0:
           return False
   return True


def calculate_primitive_root(prime):
   """Calculates the primitive root modulo a prime number."""
   if not is_prime(prime):
       raise ValueError("Input must be a prime number.")

   for candidate in range(2, prime):
       if pow(candidate, prime - 1, prime) != 1:
           continue

       powers = set(pow(candidate, powers, prime) for powers in range(1, prime - 1))
       if all(power != 1 for power in powers):
           return candidate

   raise ValueError(f"No primitive root found for the prime number {prime}.")


def diffie_hellman_key_exchange():
   """Performs the Diffie-Hellman key exchange."""
   try:
       while True:
           p = int(input("Enter a prime number (p): "))
           if is_prime(p):
               break
           print("Please enter a prime number.")

       g = calculate_primitive_root(p)

       a = int(input("Enter a private key for user1: "))
       b = int(input("Enter a private key for user2: "))

       A = pow(g, a, p)
       B = pow(g, b, p)

       shared_secret_A = pow(B, a, p)
       shared_secret_B = pow(A, b, p)

       print("\nShared Secret for user1:", shared_secret_A)
       print("Shared Secret for user2:", shared_secret_B)

   except ValueError as ve:
       print(f"Error: {ve}")
   except Exception as e:
       print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
   diffie_hellman_key_exchange()