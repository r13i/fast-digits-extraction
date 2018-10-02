from time import time

def exec_time(func):
    """
    Decorator to measure execution time of functions
    """
    def wrapper(*args, **kw):
        tic = time()
        res = func(*args, **kw)
        toc = time()
        print("*** Execution of {} :".format(func.__name__))
        print("> The result : {}".format(res))
        print("> Execution time : {} ms".format((toc - tic) * 1000), end="\n\n")
    return wrapper
