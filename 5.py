from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def generate_keys():
    # Generate RSA key pair
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(plaintext, public_key):
    # Import the public key
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    # Import the private key
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    
    # Decrypt the ciphertext
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text.decode()

# Example usage
private_key, public_key = generate_keys()
plaintext = "Hello, World!"

ciphertext = rsa_encrypt(plaintext, public_key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = rsa_decrypt(ciphertext, private_key)
print(f"Decrypted text: {decrypted_text}")