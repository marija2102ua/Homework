import cmath
def solve_quadric_equation(a, b, c):
    try:
        d = (b**2) - (4*a*c)
        sol1 = (-b-cmath.sqrt(d))/(2*a)
        sol2 = (-b+cmath.sqrt(d))/(2*a)
        return 'The solution are x1={0} and x2={1}'.format(sol1,sol2)
    except ZeroDivisionError:
        return 'Zero Division Error'
    except TypeError:
        return "Could not convert string to float"
