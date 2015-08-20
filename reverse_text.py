message = input("Type a message to be reversed: ")
encrypted = ""

i=len(message)-1
while i >= 0:
    encrypted = encrypted + message[i]
    i=i-1

print(encrypted)
    
