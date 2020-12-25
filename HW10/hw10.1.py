def age_analisys():
    age = int(input("Please enter your age: "))
    if age < 0:
        raise ValueError("age less then null")
    elif age % 2 == 0:
        print("Your age is odd")
    else:
        print("Your age is even")

if __name__ == '__main__':
    while True:
        try:
            age_analisys()
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)


