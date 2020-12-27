def divide(numerator, denominator):
    # enter your code
    try:
        return f"Result is {numerator/denominator}"
    except ZeroDivisionError:
        return f'Oops, {numerator}/0, division by zero is error!!!'
    except TypeError:
        return 'Value Error! You did not enter a number!'
