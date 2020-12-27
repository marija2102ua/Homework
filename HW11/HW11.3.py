def check_odd_even(number):
    try:
        if number%2 == 0:
            return "Entered number is even"
        return 'Entered number is odd'
    except Exception as e:
        return "You entered not a number."
