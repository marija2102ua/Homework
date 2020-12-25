def day_of_week():
    number = int(input("Please enter day number: "))
    days = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}
    print(days[number])


if __name__ == '__main__':
    while True:
        try:
            day_of_week()
        except KeyError as e:
            print('Wrong day number')
        except Exception as e:
            print(e)
