from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Pad the plaintext to be a multiple of 8 bytes
    padded_text = pad(plaintext.encode(), DES.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)
    
    return ciphertext

def des_decrypt(ciphertext, key):
    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    
    return decrypted_text.decode()

# Example usage
key = b'8bytekey'  # DES key must be 8 bytes long
plaintext = "Hello, World!"

ciphertext = des_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = des_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")