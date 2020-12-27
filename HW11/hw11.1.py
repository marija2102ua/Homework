def day_of_week(num):
    # enter your codedef day_of_week():

    try:
        int(num)
    except ValueError:
        return "You did not enter a number! Please try again."

    days = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}
    try:
        result = days[num]
    except KeyError:
        return "There is no such day of the week! Please try again."
    return result
