from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key):
    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Pad the plaintext to be a multiple of the block size
    padded_text = pad(plaintext.encode(), AES.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)
    
    return cipher.iv + ciphertext  # Prepend the IV for use in decryption

def aes_decrypt(ciphertext, key):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    
    # Create a new AES cipher object with the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text
    decrypted_text = unpad(decrypted_padded_text, AES.block_size)
    
    return decrypted_text.decode()

# Example usage
key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
plaintext = "Hello, World!"

ciphertext = aes_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = aes_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")