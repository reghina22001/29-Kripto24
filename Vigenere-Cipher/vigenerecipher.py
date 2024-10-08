def vigenere_encrypt(plaintext, key):
    """Encrypts the plaintext using the Vigenère cipher with the given key."""
    ciphertext = ""
    key_length = len(key)
    key_int = [ord(i) - ord('A') for i in key.upper()]
    plaintext_int = [ord(i) - ord('A') for i in plaintext.upper() if i.isalpha()]

    for i in range(len(plaintext_int)):
        # Perform encryption
        value = (plaintext_int[i] + key_int[i % key_length]) % 26
        ciphertext += chr(value + ord('A'))

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the Vigenère cipher with the given key."""
    plaintext = ""
    key_length = len(key)
    key_int = [ord(i) - ord('A') for i in key.upper()]
    ciphertext_int = [ord(i) - ord('A') for i in ciphertext.upper() if i.isalpha()]

    for i in range(len(ciphertext_int)):
        # Perform decryption
        value = (ciphertext_int[i] - key_int[i % key_length] + 26) % 26
        plaintext += chr(value + ord('A'))

    return plaintext


def main():
    print("Vigenère Cipher")
    print("-----------------")
    
    # Input plaintext
    plaintext = input("Masukkan kalimat (plaintext): ").replace(" ", "").upper()
    
    # Validate key input
    while True:
        key = input("Masukkan kunci (hanya huruf): ").replace(" ", "").upper()
        if key.isalpha():
            break
        print("Kunci tidak valid. Harap masukkan hanya huruf.")

    # Enkripsi
    ciphertext = vigenere_encrypt(plaintext, key)
    print("\nHasil Enkripsi:", ciphertext)

    # Dekripsi
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("Hasil Dekripsi:", decrypted_text)


if __name__ == "__main__":
    main()
