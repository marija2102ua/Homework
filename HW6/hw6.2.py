from modules.square import rectangle, triangle, circle


def main():
    while True:
        num = input("""What do you want to calculate?
1.calculates the square of a rectangle
2.calculates the square of triangle
3.calculates the square of circle
Your choice: """)
        if num == "1":
            sideA = float(input("Enter A: "))
            sideB = float(input("Enter B: "))
            print(f'Square: {rectangle(sideA, sideB)}')
        elif num == "2":
            sideA = float(input("Enter A: "))
            sideB = float(input("Enter B: "))
            sideC = float(input("Enter C: "))
            print(f'Square: {triangle(sideA, sideB, sideC)}')

        elif num == "3":
            radius = float(input("Enter radius: "))
            print(f'Square: {circle(radius)}')
        else:
            print("Please make a choice")


if __name__ == '__main__':
    main()
