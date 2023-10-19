def recusive_mul(m, n):
    if n == 1:
        return m
    else:
        return (m, n-1) + m

def is_prime(n):
    if(n == 1):
        return "Undefined"
    def helper_is_prime(n, k):
        if k > 1:
            if n % k == 0:
                return False
            else:
                return helper_is_prime(n, k-1) 
        return True
    return helper_is_prime(n, n-1)

def count_stair_ways(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_stair_ways_of_k(n, k):
    if n == 1:
        return 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum([count_stair_ways_of_k(n - diff_k, k)  for diff_k in range(1, k + 1)])

def even_weights(s):
    return [s[::2][x] * 2 * x for x in range(len(s[::2]))] 

def max_product(s):
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return max(s[0], s[1])
    else:
        return_lst = [s[x] * max_product(s[x+2:]) for x in range(len(s))]
        return max(return_lst)

def check_hole_number(x):
    if len(str(x)) == 1:
        return True
    for i in range(0, len(str(x))-2, 2):
        if int(str(x)[i]) < int(str(x)[i+1]) or int(str(x)[i+2]) < int(str(x)[i+1]):
            return False
    return True

def check_mountain_number(x):
    lst_x = list(map(int, list(str(x))))
    print(lst_x)
    def up(lst_x):
        if len(lst_x) == 1:
            return True
        for x in range(0, len(lst_x) - 1):
            if not lst_x[x] < lst_x[x + 1]:
                    return False
        return True
    def down(lst_x):
        if len(lst_x) == 1:
            return True
        for x in range(0, len(lst_x) - 1):
            if not lst_x[x] > lst_x[x + 1]:
                    return False
        return True
    max_ind = lst_x.index(max(lst_x))
    print(lst_x[:max_ind], lst_x[max_ind:])
    return up(lst_x[:max_ind]) and down(lst_x[max_ind:])
    
