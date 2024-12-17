def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += new_char
        else:
            decrypted_text += char
    
    return decrypted_text

if __name__ == "__main__":
    ciphertext = input("Masukkan teks terenkripsi: ")
    shift = int(input("Masukkan jumlah shift (kunci): "))
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print("Teks setelah dekripsi:", decrypted_text)
