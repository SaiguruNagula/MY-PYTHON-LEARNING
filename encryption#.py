import random 
import string

charset = list(string.ascii_letters + string.digits + string.punctuation + " ") # Including space for better readability

key = charset.copy()
random.shuffle(key)  # Shuffle the key to create a random mapping

print(charset)
print()
print()  
print(key)


def encrypt(text, key,charset ):
    encrypt_text=""
    for letter in text:
        ind = charset.index(letter)
        encrypt_text += key[ind]

    return encrypt_text

def decrypt(encrypted_text, key, charset):
    decrypt_text = ""
    for letter in encrypted_text:
        ind = key.index(letter)
        decrypt_text += charset[ind]

    return decrypt_text

def main():
    is_running = True  
    while is_running:
      print("Welcome to the Encryption Program!")
      val= input("enter 1 for text encryption and 2 for decription : ")
      if val not in ['1', '2']:
          print("Invalid choice. Please enter 1 for encryption or 2 for decryption.")
          continue
      if val == '1':
       text = input("Enter the text to encrypt: ")
       encrypted_text = encrypt(text, key,charset)
       print(f"Encrypted text: {encrypted_text}")
       continue 
      elif val == '2':
       text = input("Enter the text to encrypt: ")
       decrypted_text = decrypt(encrypted_text, key, charset)
       print(f"Decrypted text: {decrypted_text}")
       continue
      else:
         print("Invalid choice. Please enter 1 for encryption or 2 for decryption.")
      print("Thank you for using the Encryption Program!")
      print("Do you want to continue? (yes/no)")
      continue_choice = input("Enter your choice (yes/no): ").strip().lower()
      if continue_choice != 'yes':
          print("Thank you for using the Encryption Program!")
          is_running = False



if __name__ == "__main__":
    main()

