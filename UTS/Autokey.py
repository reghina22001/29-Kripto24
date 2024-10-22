def generate_extended_key(plaintext, key):
    """
    Menghasilkan kunci yang diperpanjang berdasarkan panjang plaintext.
    """
    # Menghapus spasi dan mengubah menjadi huruf besar
    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    
    # Mulai dengan kunci, kemudian tambahkan karakter plaintext sesuai panjang plaintext
    extended_key = key
    for i in range(len(plaintext) - len(key)):
        extended_key += plaintext[i]  # Tambahkan karakter dari plaintext
        
    return extended_key

def autokey_cipher(plaintext, key):
    """
    Melakukan enkripsi menggunakan Autokey Cipher.
    """
    # Ubah plaintext dan key menjadi uppercase dan hilangkan spasi
    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    
    # Hasilkan extended key yang sesuai panjang plaintext
    extended_key = generate_extended_key(plaintext, key)
    ciphertext = []
    
    for i, p in enumerate(plaintext):
        # Menghitung posisi huruf di alfabet (A=0, B=1, ..., Z=25)
        p_index = ord(p) - ord('A')
        k_index = ord(extended_key[i]) - ord('A')
        
        # Enkripsi
        c_index = (p_index + k_index) % 26
        ciphertext.append(chr(c_index + ord('A')))
    
    return ''.join(ciphertext)

def autokey_decrypt(ciphertext, key):
    """
    Melakukan dekripsi menggunakan Autokey Cipher.
    """
    # Ubah ciphertext dan key menjadi uppercase dan hilangkan spasi
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    
    # Extended key dimulai dari key asli
    extended_key = key
    plaintext = []
    
    for i, c in enumerate(ciphertext):
        # Menghitung posisi huruf di alfabet (A=0, B=1, ..., Z=25)
        c_index = ord(c) - ord('A')
        k_index = ord(extended_key[i]) - ord('A')
        
        # Dekripsi
        p_index = (c_index - k_index) % 26
        plaintext.append(chr(p_index + ord('A')))
        
        # Perbarui extended key dengan huruf plaintext yang baru terdekripsi
        extended_key += plaintext[-1]  # Tambahkan huruf plaintext yang baru terdekripsi
    
    return ''.join(plaintext)

# Meminta input dari pengguna
plaintext = input("Masukkan plaintext: ")
key = input("Masukkan kunci: ")

# Menjalankan Autokey Cipher untuk enkripsi
ciphertext = autokey_cipher(plaintext, key)
extended_key = generate_extended_key(plaintext, key)

# Menampilkan hasil enkripsi
print("\nPlaintext:", plaintext)
print("Kunci:", key)
print("Extended Key:", extended_key)
print("Ciphertext:", ciphertext)

# Menjalankan Autokey Cipher untuk dekripsi
decrypted_text = autokey_decrypt(ciphertext, key)

# Menampilkan hasil dekripsi
print("\nCiphertext yang didekripsi:", ciphertext)
print("Plaintext yang terdekripsi:", decrypted_text)
