# Converts string to 8-bit byte (i.e., keeps the "leading zero")

message = input("Please type the message you would like to convert to binary: ")

binary_message = " ".join(format(ord(x), "08b") for x in message)

print(binary_message)
