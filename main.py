import numpy as np
from time import time


def exp_by_squaring(base, exp):
    """
    Homemade expo by squaring method based on well-known algorithm
    @wiki `https://en.wikipedia.org/wiki/Exponentiation_by_squaring`
    """
    if exp == 0:
        return 1
    if exp < 0:
        base = 1 / base
        exp = -exp
    res = 1
    while exp > 1:
        if exp % 2:
            res = res * base
            base = base * base
            exp = (exp - 1) / 2
        else:
            base = base * base
            exp = exp / 2
    return base * res


def exec_time(func):
    """
    Decorator to measure execution time of functions
    """
    def wrapper(*args, **kw):
        tic = time()
        res = func(*args, **kw)
        toc = time()
        print("*** Execution of {} :".format(func.__name__))
        # print("> The result : {}".format(res))
        print("> Execution time : {} ms".format((toc - tic) * 1000))
    return wrapper



@exec_time
def exec1(n):
    return np.power(n, n)

@exec_time
def exec2(n):
    return pow(n, n)

@exec_time
def exec3(n):
    return exp_by_squaring(n, n)

if __name__ == "__main__":

    print("Start ...")
    exec1(12345)
    exec2(12345)
    exec3(12345)