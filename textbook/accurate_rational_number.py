# Since store fractional numbers as float 
# will lead to float approximation
# So create the data type to store numerator and donominator
# Use Function to process it.

from fractions import gcd
# To finish this part, just use wishful think 
# and don't consider the implement.
def add_rationals(x, y):
    nx, dx = numer(x), donom(x)
    ny, dy = numer(y), donom(y)
    return rational(nx*dy + ny*dx, dx*dy)

def mul_rationals(x,y):
    return rational(numer(x)*numer(y), donom(x)*donom(y))

def print_rationals(x):
    print(numer(x), "/", donom(x))

def rationals_are_equal(x, y):
    return numer(x)*donom(y) == numer(y)*donom(x)

def rational(n, d):
    g = gcd(n, d)
    return [n//g, d//g]

def numer(x):
    return x[0]

def donom(x):
    return x[1]
