from math import sqrt, pow, pi


def rectangle(side_a, side_b):
    """
 this function calculates the rectangle
    """
    return side_a * side_b


def triangle(side_a, side_b, side_с):
    p = (side_a + side_b + side_с) / 2
    return sqrt(p * (p - side_a) * (p - side_b) * (p - side_с))

def circle(R):
    return pi * pow(R, 2)


if __name__ == '__main__':
    pass