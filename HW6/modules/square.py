PI = 3.14


def rectangle(side_a, side_b):
    """
 this function calculates the rectangle
    """
    return side_a * side_b


def triangle(side_a, side_b, side_c):
    p = (side_a + side_b + side_c) / 2
    return (p * (p - side_a) * (p - side_b) * (p - side_c))**(1/2)

def circle(R):
    return PI * R**2

if __name__ == '__main__':
    pass