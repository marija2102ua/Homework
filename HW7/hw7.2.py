import re
m = input("Please enter your password: ")
x = True

while x:
    if (len(m)<6 or len(m)>16):
        break
    elif not re.search("[a-z]",m):
        break
    elif not re.search("[A-Z]",m):
        break
    elif not re.search("[0-9]",m):
        break
    elif not re.search("[$#@]",m):
        break
    else:
        print("valid password")
        x = False
        break

if x:
    print("Not a valid password")