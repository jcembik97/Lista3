import base64

def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text):
    try:
        decoded_bytes = base64.b64decode(text)
        decoded_text = decoded_bytes.decode()
        return decoded_text
    except base64.binascii.Error:
        return "Error during decryption. Make sure the text is correctly encoded."

while True:
    # Ask the user for text to encrypt or decrypt
    user_choice = input("Choose an option:\n1. Encrypt text\n2. Decrypt text\n3. Exit\n")

    if user_choice == "1":
        original_text = input("Enter text to encrypt: ")
        encrypted_text = base64_encrypt(original_text)
        print('Encrypted:', encrypted_text)
    elif user_choice == "2":
        encrypted_text = input("Enter text to decrypt: ")
        decrypted_text = base64_decrypt(encrypted_text)
        print('Decrypted:', decrypted_text)
    elif user_choice == "3":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice. Choose 1, 2, or 3.")
