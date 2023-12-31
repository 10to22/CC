
import tkinter as tk
from tkinter import *

def pigpen_cipher(text):
    pigpen_key = {
        'A': '🔵🔘🔵 ',
        'B': '🔵🔘🔘 ',
        'C': '🔘🔘🔵 ',
        'D': '🔘🔘🔘 ',
        'E': '🔵🔵🔘 ',
        'F': '🔵🔵🔵 ',
        'G': '🔵🔴🔘 ',
        'H': '🔵🔴🔵 ',
        'I': '🔴🔘🔘 ',
        'J': '🔴🔘🔵 ',
        'K': '🔴🟣🔘 ',
        'L': '🔴🔴🔵 ',
        'M': '🔴🔵🔘 ',
        'N': '🔴🔵🔵 ',
        'O': '🔘🔴🔘 ',
        'P': '🔘🔴🔵 ',
        'Q': '🔴🔵🔴 ',
        'R': '🔴🔴🔴 ',
        'S': '🔵🔴🟣 ',
        'T': '🔵🔵🔴 ',
        'U': '🔘🔴🔴 ',
        'V': '🔘🔵🔴 ',
        'W': '🔵🔴🔴 ',
        'X': '🔴🔘🔴 ',
        'Y': '🔴🔴🔘 ',
        'Z': '🔵🔘🔴 ',
        ' ': '🟡🟠🟡 ',
        '!': '🟡🟠🔴 ',
        '.': '🟡🟠🔘 ',
        '?': '🟡🟠🔵 ',
        ',': '🟡🔘🟠 ',
        '0': '🔴🟠🟤 ',
        '1': '🟤🔴🟠 ',
        '2': '🟡🔘🔴 ',
        '3': '🔘🟠🔵 ',
        '4': '🔵🟤🟠 ',
        '5': '🟡🔵🟤 ',
        '6': '🔘🟠🟤 ',
        '7': '🟤🟠🟠 ',
        '8': '🟡🟠🟤 ',
        '9': '🟡🟤🟠 '
    }

    text = text.upper()
    encrypted_text = ""
    for char in text:
        if char in pigpen_key:
            encrypted_text += pigpen_key[char]

    return encrypted_text

def pigpen_decipher(encrypted_text):
    pigpen_key = {
        '🔵🔘🔵': 'A',
        '🔵🔘🔘': 'B',
        '🔘🔘🔵': 'C',
        '🔘🔘🔘': 'D',
        '🔵🔵🔘': 'E',
        '🔵🔵🔵': 'F',
        '🔵🔴🔘': 'G',
        '🔵🔴🔵': 'H',
        '🔴🔘🔘': 'I',
        '🔴🔘🔵': 'J',
        '🔴🟣🔘': 'K',
        '🔴🔴🔵': 'L',
        '🔴🔵🔘': 'M',
        '🔴🔵🔵': 'N',
        '🔘🔴🔘': 'O',
        '🔘🔴🔵': 'P',
        '🔴🔵🔴': 'Q',
        '🔴🔴🔴': 'R',
        '🔵🔴🟣': 'S',
        '🔵🔵🔴': 'T',
        '🔘🔴🔴': 'U',
        '🔘🔵🔴': 'V',
        '🔵🔴🔴': 'W',
        '🔴🔘🔴': 'X',
        '🔴🔴🔘': 'Y',
        '🔵🔘🔴': 'Z',
        '🟡🟠🟡': ' ',
        '🟡🟠🔴': '!',
        '🟡🟠🔘': '.',
        '🟡🟠🔵': '?',
        '🟡🔘🟠': ',',
        '🔴🟠🟤': '0',
        '🟤🔴🟠': '1',
        '🟡🔘🔴': '2',
        '🔘🟠🔵': '3',
        '🔵🟤🟠': '4',
        '🟡🔵🟤': '5',
        '🔘🟠🟤': '6',
        '🟤🟠🟠': '7',
        '🟡🟠🟤': '8',
        '🟡🟤🟠': '9'
    }

    decrypted_text = ""
    encrypted_text = encrypted_text.split()
    for symbol in encrypted_text:
        if symbol in pigpen_key:
            decrypted_text += pigpen_key[symbol]

    return decrypted_text

def encrypt_message():
    message = input_text.get("1.0", tk.END).strip()
    encrypted_message = pigpen_cipher(message)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_message)
    output_text.config(state=tk.DISABLED)

def decrypt_message():
    encrypted_message = input_text.get("1.0", tk.END).strip()
    decrypted_message = pigpen_decipher(encrypted_message)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_message)
    output_text.config(state=tk.DISABLED)

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))

def paste_input():
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, root.clipboard_get())

def export_message():
    message = output_text.get("1.0", tk.END).strip()
    with open("output.txt", "w") as file:
        file.write(message)
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Spark Cipher Encryption")

    root.resizable(width=False, height=False)

    input_text = tk.Text(root, wrap=tk.WORD, height=5)  # Set height to 5 rows
    output_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)

    encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, font=("Arial", 14), width=10)
    decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message, font=("Arial", 14), width=10)
    copy_button = tk.Button(root, text="Copy", command=copy_output, font=("Arial", 14), width=10)
    paste_button = tk.Button(root, text="Paste", command=paste_input, font=("Arial", 14), width=10)
    export_button = tk.Button(root, text="Export", command=export_message, font=("Arial", 14), width=10)
    clear_button = tk.Button(root, text="Clear", command=clear_text, font=("Arial", 14), width=10)

    clear_button.grid(row=0, column=5, padx=5, pady=5, sticky='nw')
    encrypt_button.grid(row=0, column=0, padx=(10, 5), pady=5, sticky='nw')
    decrypt_button.grid(row=0, column=1, padx=5, pady=5, sticky='nw')
    copy_button.grid(row=0, column=2, padx=5, pady=5, sticky='nw')
    paste_button.grid(row=0, column=3, padx=5, pady=5, sticky='nw')
    export_button.grid(row=0, column=4, padx=(5, 10), pady=5, sticky='nw')
    input_text.grid(row=1, column=0, columnspan=6, padx=10, pady=5, sticky='nsew')
    output_text.grid(row=2, column=0, columnspan=6, padx=10, pady=5, sticky='nsew')

    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()