def keep_ints(cond, x):
    for i in range(x+1):
        if cond(i) == 1:
            print(i)

def make_keeper(arg2):
    def curry_inner(arg1):
        return keep_ints(arg1, arg2)
    return curry_inner

def is_even(x):
    return x % 2 == 0

def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print
