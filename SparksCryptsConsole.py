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

def main():
    while True:
        print("Pigpen Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter the text to encrypt: ")
            encrypted_message = pigpen_cipher(message)
            print("Encrypted message:")
            print(encrypted_message)
        elif choice == "2":
            encrypted_message = input("Enter the encrypted text: ")
            decrypted_message = pigpen_decipher(encrypted_message)
            print("Decrypted message:")
            print(decrypted_message)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()