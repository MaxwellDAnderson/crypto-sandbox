import os
import sys
import time
import pgpy
from pgpy import PGPMessage
from pgpy import PGPKey


greeting = input("Would you like to transmit an encrypted message? (Y)/(N) ").lower()
print(greeting)

if greeting == "n":
    sys.exit("Okay. Goodbye.")

while greeting != "y" and greeting != "n":
    invalid_entry = "You have entered an invalid choice. Please select either Y or N, followed by the Enter/Return key."
    print(invalid_entry)
    second_greeting = input("Do you still want to transmit an encrypted message? (Y)/(N) ").lower()
    print(second_greeting)
    if second_greeting != "y" and second_greeting != "n":
        continue
    elif second_greeting == "y":
        greeting = second_greeting
        break
    elif second_greeting == "n":
        sys.exit("Okay. Goodbye.")



path = "C:/Users/MDA/Desktop/pgpkeys" #/path/to/public/key/directory"
file_names = os.listdir(path)
separator = "-"
file_numbers = [x for x in range(len(file_names)) if x <= len(file_names)]

for i in range(len(file_numbers)):
    print(file_numbers[i], separator, file_names[i])

while True:
    try:
        key_selection = int(input("Please enter the number of the message recipient: "))
    except ValueError:
        print("You have not entered a number. Please try again.")
        continue
    else:
        if key_selection <= len(file_numbers) - 1:
            message_recipient = file_names[key_selection]
            break
        elif key_selection > len(file_numbers) - 1:
            print("You have entered an invalid number. Please try again.")
            continue


key_path = path + "/" + message_recipient


pubkey, _ = PGPKey.from_file(key_path)
msg = PGPMessage.new(input("Please type your message: "))
pubkey.encrypt(msg)
print("\n")
print("THANK YOU. YOUR ENCRYPTED MESSAGE IS PRINTED BELOW:\n \n")
print(pubkey.encrypt(msg))
print("\n")

sys.exit("This program is terminating operations.")
