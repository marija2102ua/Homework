class MyError(Exception):
    pass
    # enter your code


def check_positive(number):
    # enter your code
    try:
        if float(number) < 0:
            raise MyError(f"You input negative number: {float(number)}. Try again.")
    except MyError as e:
        return e
    except Exception:
        return "Error type: ValueError!"
    else:
        return f"You input positive number: {float(number)}"
    