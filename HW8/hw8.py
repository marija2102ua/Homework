class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f'Please enter side {str(i+1)}: '))
                      for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n):
            print(f'Side {i+1} is {self.sides[i]}')


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
        #Polygon.__init__(self, 2)

    def rectangle_area(self):
        a, b = self.sides
        return a*b


rect = Rectangle()

rect.inputSides()
rect.displaySides()

print(rect.rectangle_area())