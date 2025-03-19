import Logo

def encrypt_message():
    message = input("Type your message: ")
    shift_count = input("How many shifts per letter: ")
    crypted_message = ""
    for i in message:
        char = ord(i)
        new_char = char + int(shift_count)
        crypted_message += chr(new_char)

    print(f"Your crypted message is: {crypted_message}")
    
def decrypt_message():
    message = input("What is your message to decrypt: ")
    shift_count = input("How many shifts per letter: ")
    decrypted_message = ""
    for i in message:
        char = ord(i)
        new_char = char - int(shift_count)
        decrypted_message += chr(new_char)
        
    print(f"Your decrypted message is: {decrypted_message}")    
    
def caesar_cypher():
    stop = False
    while not stop:
        user_choice = input("Type encrypt/decrypt for processing your message : ").lower()
        if user_choice == "encrypt":
            print("You chose to encrypt a message ! \n")
            encrypt_message()
            user_want_to_continue = input("Do you want to try again (yes/no): ").lower()
            if user_want_to_continue == "no":
                stop = True
        elif user_choice == "decrypt":
            print("You chose to decrypt a message ! \n")
            decrypt_message()
            user_want_to_continue = input("Do you want to try again (yes/no): ").lower()
            if user_want_to_continue == "no":
                stop = True
    
    
    

print(Logo.logo)
caesar_cypher()

