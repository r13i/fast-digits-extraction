from time import time
from exec_time import exec_time

def digits_extract_1(n):
    units = n % 10
    tens = int((n % 100) / 10)
    return (units, tens)

def digits_extract_2(n):
    units = n % 10
    tens = int((n / 10) % 10)
    return (units, tens)


@exec_time
def exec1(n):
    return digits_extract_1(n)

@exec_time
def exec2(n):
    return digits_extract_2(n)


if __name__ == "__main__":

    n = 123456789

    exec1(n)
    exec2(n)