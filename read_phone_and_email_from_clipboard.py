import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code in format of 555 or (555) (optional)
    (\s|-|\.)?                      #separator, either space, - or . (optional)
    (\d{3})                         #first 3 digits
    (\s|-|\.)                       #separator again
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
    )''',re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9._%+-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_number += ' x' + groups[8]
    matches.append(phone_number)
for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard: ")
    print('\n'.join(matches))
else:
    print("No phone numbers of email addresses found!")
