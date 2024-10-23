def encrypt_message(message, key):
    # Create an empty list to store the ciphertext
    ciphertext = [''] * key

    # Loop through each column in the ciphertext
    for column in range(key):
        current_index = column

        # Loop through each character in the message
        while current_index < len(message):
            # Place the character in the correct column
            ciphertext[column] += message[current_index]
            # Move to the next row in the column
            current_index += key

    # Join the columns to get the final ciphertext
    return ''.join(ciphertext)

def decrypt_message(ciphertext, key):
    # Calculate the number of columns and rows
    num_columns = int(len(ciphertext) / key)
    num_rows = key
    num_shaded_boxes = (num_columns * num_rows) - len(ciphertext)

    # Create an empty list to store the plaintext
    plaintext = [''] * num_columns

    # Initialize variables to track the current column and row
    column = 0
    row = 0

    # Loop through each character in the ciphertext
    for symbol in ciphertext:
        plaintext[column] += symbol
        column += 1

        # If we've reached the end of a column or a shaded box, move to the next row
        if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - num_shaded_boxes):
            column = 0
            row += 1

    # Join the columns to get the final plaintext
    return ''.join(plaintext)

# Example usage
message = "Hello World"
key = 3

encrypted = encrypt_message(message, key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_message(encrypted, key)
print(f"Decrypted: {decrypted}")