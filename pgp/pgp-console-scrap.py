# This was the first file I tried writing the PGP console program in. I
# eventually decided to start fresh and incoroporate portions of this file
# into the final file.

import os
import sys
import time
import pgpy
from pgpy import PGPMessage
from pgpy import PGPKey

path = "C:/Users/MDA/Desktop/pgpkeys"
listdir = list(enumerate(os.listdir(path)))
# w = len(listdir)
# x = int(w)

class file_index:

    def append_list():
        for y in listdir:
            file_numbers = []
            x = 0
            file_numbers.append(listdir[x][0])
            x += 1
    def list_string():
        list_strings = [str(x) for z in self.append_list.file_numbers]

file_index.append_list()
file_index.list_strings()

# create_file_index()
# file_index_as_strings = [str(x) for x in file_index.create_file_index()]



greeting = input("Would you like to transmit an encrypted message? (Y)/(N) ").lower()
print(greeting)
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


i = 0
for x in listdir:
    print(listdir[i])
    i += 1



t1 = input("Please enter the number of the recipient from the list above: ")

while t1 not in file_index_as_strings:
    t1_take_two = input("You have entered an invalid recipient. Please enter the number of the recipient: ")
    print(t1_take_two)
    if t1 not in file_index_as_strings:
        continue
    elif t1 == x in file_index_as_strings:
        t1_take_two = int(t1)
        break




# KEY LOADING
selected_public_key = listdir[int(t1)][1]

public_key_path = path + selected_public_key

print(public_key_path)




'''
    try:
        t1 = input("Please enter the number of the recipient: ")
        break
    except t1 > len(listdir):
        raise ValueError
        print("You have entered an invalid recipient. Please try again: ")
    except t1.isdigit() is False:
        raise TypeError
        print("You have entered an invalid recipient. Please try again: ")
        continue
    finally:
        if int(t1) <= len(listdir) - 1:
            t1 = int(t1)
            break
'''



'''
while t1.isnumeric() is False:
    t1_take_two = input("You have not entered an integer. Please try again: ")
    print(t1_take_two)
    if t1_take_two.isnumeric() is False:
        continue
    else:
        t1 = t1_take_two
        break

while int(t1) > len(listdir) - 1:
    t1_take_three = input("You have entered an invalid recipient. Please try again: ")
    print(t1_take_three)
    if int(t1_take_three) > len(listdir) - 1:
        continue
    elif int(t1_take_three) <= len(listdir) - 1 and t1_take_three.isnumeric():
        t1 = t1_take_three
        t1 = int(t1)
        break

'''

print("YES!")


'''
tuple_number = input(int("Please enter the number of the recipient: "))
print(tuple_number)
while tuple_number > len(listdir) - 1:
    invalid_recipient = "You have entered an invalid recipient, please try again."
    print(invalid_recipient)

    print(tuple_number)
    if

'''






index_b = input(int())





'''

numbered_files = enumerate(listdir)

for i, item in enumerate(listdir, 0):
    print(i, ". " + item)
    i+= 1
'''





# ///
