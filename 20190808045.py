import random
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    """ Generate an odd integer randomly. """
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """ Generate a prime number of specified bit length. """
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keys(bit_length=16):
    """ Generate RSA public and private keys. """
    p = generate_prime_number(bit_length // 2)
    q = generate_prime_number(bit_length // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Commonly used prime for e
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    """ Encrypt plaintext using the public key. """
    e, n = public_key
    plaintext_numbers = [ord(char) for char in plaintext]
    ciphertext = [pow(m, e, n) for m in plaintext_numbers]
    return ciphertext

def decrypt(private_key, ciphertext):
    """ Decrypt ciphertext using the private key. """
    d, n = private_key
    plaintext_numbers = [pow(c, d, n) for c in ciphertext]
    plaintext = ''.join([chr(m) for m in plaintext_numbers])
    return plaintext

# Example usage
if __name__ == "__main__":
    public_key, private_key = generate_keys(16)
    message = "Hello Elliot Alderson"
    print("Original Message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted Message:", decrypted_message)
