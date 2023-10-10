# 
def path(m, n):
    """Return the number of paths from one corner
    of an M * N grid to the opposite of the corner
    
    >>>path(2, 2)
    2
    >>>path(5, 7)
    210
    >>>path(117, 1)
    1
    >>>path(1, 157)
    1
    """
    # So in a specific position, there is exactly two directions to go:
    # go right or go up. So the problem is simplfied to sum of methods that
    # the left position of current and the down position of current take a step use
    if m == 1 or n == 1:
        return 1
    else:
        return path(m-1, n) + path(m, n-1)

def knap(n, k):
    """Return whether there exists an combination of digits in n
    that the sum is equal to k
    """
    if n == 0:
        return k == 0
    with_last = knap(n//10, k-n%10)
    without_last = knap(n//10, k-n%10)
    return with_last or without_last

def count_partition(n, m):
    """The number of partitions of a positive integer n,
    using parts up to size m, is the number of waysin which
    n can be expressed as the sum of positive integer 
    parts up to m in nondecreasing order
    """
    if n == 0:
        return 1
    elif m == 0:
        return 0
    elif n < 0:
        return 0
    with_m = count_partition(n-m, m)
    without_m = count_partition(n, m-1)
    return with_m + without_m 

def all_nums(k):
    """Recusively print binary number with n digits in nondecreasing order
    For example:
    >>>all_nums(3)
    0
    1
    10
    11
    100
    101
    110
    111
    """
    # Can consider the above example in the way that
    # 000 001 010 011 100 101 110 111
    # Use prefix to record the first digit
    def help(k, prefix):
        if k == 0:
            print(prefix)
            return
        help(k-1, prefix*10)
        help(k-1, prefix*10+1)
    help(k, 0)
