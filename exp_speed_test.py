import numpy as np

from exec_time import exec_time


def exp_by_squaring(base, exp):
    """
    Homemade power function by squaring method based on well-known algorithm
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
    exec1(123)
    exec2(123)
    exec3(123)
