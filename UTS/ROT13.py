# Fungsi untuk enkripsi dan dekripsi menggunakan ROT13
def rot13(text):
    result = ''
    for char in text:
        # Memeriksa apakah karakter adalah huruf
        if char.isalpha():
            # Menentukan offset tergantung dari apakah karakter huruf besar atau kecil
            offset = 65 if char.isupper() else 97
            # Menggeser karakter dengan 13 posisi dalam alfabet
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            # Jika bukan huruf, biarkan karakter tidak berubah
            result += char
    return result

# Input dari pengguna
plain_text = input("Masukkan teks yang ingin dienkripsi menggunakan ROT13: ")

# Melakukan enkripsi menggunakan ROT13
cipher_text = rot13(plain_text)
print("Hasil Enkripsi (ROT13):", cipher_text)  # Menambahkan newline sebelum hasil enkripsi

# Melakukan dekripsi (karena ROT13 simetris, gunakan fungsi yang sama)
decrypted_text = rot13(cipher_text)
print("\nHasil Dekripsi:", decrypted_text) 