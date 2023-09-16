def pow(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance = 1e-3):
    return abs(x - y) < tolerance

def newton_update(f, df):
    def update(x):
        return x - f(x)/df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero )

def nth_root_of_a(n, a):
    def f(x):
        return pow(x, n) - a
    def df(x):
        return n * pow(x, n-1)
    return find_zero(f, df)
