def curry_f(f):
    def g(x):
        def ori(y):
            return ori(x, y)
        return res
    return g

def uncurry_f(f):
    def res(x, y):
        return f(x, y):
    return res
