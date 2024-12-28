import rsa

# Step 1: Generate RSA keys
(public_key, private_key) = rsa.newkeys(512)

# Step 2: Define the message
message = "Hello Elliot Alderson".encode('utf-8')  # Convert to bytes

# Step 3: Encrypt the message using the public key
encrypted_message = rsa.encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

# Step 4: Decrypt the message using the private key
decrypted_message = rsa.decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message.decode('utf-8'))
