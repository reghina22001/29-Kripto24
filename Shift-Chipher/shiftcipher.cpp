#include <iostream>
#include <string>

using namespace std;

string encrypt(string text, int shift) {
    string result = "";

    // Loop untuk setiap karakter dalam teks
    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        // Periksa apakah huruf adalah alfabet
        if (isalpha(ch)) {
            char base = isupper(ch) ? 'A' : 'a';
            // Geser huruf dan simpan hasil
            result += char(int(base + (ch - base + shift) % 26));
        } else {
            // Jika bukan huruf, tambahkan karakter asli
            result += ch;
        }
    }
    return result;
}

string decrypt(string text, int shift) {
    // Dekripsi adalah kebalikan dari enkripsi
    return encrypt(text, 26 - shift);
}

int main() {
    string text;
    int shift;

    cout << "Masukkan Teks: ";
    getline(cin, text);
    cout << "Masukkan Jumlah Key: ";
    cin >> shift;

    string encrypted = encrypt(text, shift);
    string decrypted = decrypt(encrypted, shift);

    cout << "Teks Terenkripsi: " << encrypted << endl;
    cout << "Teks Terdekripsi: " << decrypted << endl;

    return 0;
}