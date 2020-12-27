import re
def is_valid(email):
    pattern = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\.-]+\.[a-zA-Z]*$")
    if re.match(pattern,email):
        return "Email is valid"
    else:
        raise ValueError("Email is not valid")



def valid_email(email):
    try:
        return is_valid(email)
    except ValueError as e:
        return e