import re

def check_password(pw):
    length_regex = re.compile(r'.{8}') #has at least 8 chars
    mo = length_regex.search(pw)
    if(mo==None):
        print("Password must be at least 8 characters long!")
        return False

    upper_regex = re.compile(r'[A-Z]') #has at least 1 upper
    mo = upper_regex.search(pw)
    if(mo==None):
        print("Password must contain at least 1 uppercase letter!")
        return False

    lower_regex = re.compile(r'[a-z]') #has at least 1 lower
    mo = lower_regex.search(pw)
    if(mo==None):
        print("Password must contain at least 1 lowercase letter!")
        return False
    
    num_regex = re.compile(r'[0-9]') #has at least 1 number
    mo= num_regex.search(pw)
    if(mo==None):
        print("Password must contain at least one number!")
        return False

    print("Password accepted!")
    return True

check_password('hello') #less than 8 chars
check_password('helloooooooooo') #no upper
check_password('HELLLOOOOOOOOOO') # no lower
check_password('Helllooooooooooo') #no number
