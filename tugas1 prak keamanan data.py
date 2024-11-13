import tkinter as tk
from tkinter import messagebox

# Fungsi Caesar Cipher untuk Enkripsi
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Fungsi Caesar Cipher untuk Dekripsi
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Fungsi untuk tombol Enkripsi
def encrypt_text():
    text = input_text.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_encrypt(text, shift)
    output_text.delete(0, tk.END)
    output_text.insert(0, encrypted_text)

# Fungsi untuk tombol Dekripsi
def decrypt_text():
    text = input_text.get()
    shift = int(shift_entry.get())
    decrypted_text = caesar_decrypt(text, shift)
    output_text.delete(0, tk.END)
    output_text.insert(0, decrypted_text)

# Membuat GUI dengan tkinter
app = tk.Tk()
app.title("Aplikasi Caesar Cipher")
app.geometry("400x200")

# Label dan Entry untuk Input Text
tk.Label(app, text="Masukkan Teks:").pack()
input_text = tk.Entry(app, width=50)
input_text.pack()

# Label dan Entry untuk Shift
tk.Label(app, text="Masukkan Shift (angka):").pack()
shift_entry = tk.Entry(app, width=10)
shift_entry.pack()

# Tombol Enkripsi dan Dekripsi
tk.Button(app, text="Enkripsi", command=encrypt_text).pack(pady=5)
tk.Button(app, text="Dekripsi", command=decrypt_text).pack(pady=5)

# Entry untuk Output Text
tk.Label(app, text="Hasil:").pack()
output_text = tk.Entry(app, width=50)
output_text.pack()

# Menjalankan GUI
app.mainloop()
