class ToSmallNumberGroupError(BaseException):
    pass
    # enter your code


def check_number_group(number):
    try:
        if int(number)>=10:
            return f"Number of your group {int(number)} is valid"
        else:
            raise ToSmallNumberGroupError
    except ToSmallNumberGroupError:
        return "We obtain error:Number of your group can't be less than 10"
    except Exception:
        return "You entered incorrect data. Please try again."