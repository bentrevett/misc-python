def reverse_text(string):
    backwards=""
    i=len(string)-1
    while i >= 0:
        backwards+=string[i]
        i-=1
    return backwards

while True:
    message = input("Type some text to be reversed: ")
    print(reverse_text(message))
    
