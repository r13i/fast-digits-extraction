from time import time
from numpy import mean

# def exec_time(func, n_iter=1):
#     """
#     Decorator to measure te average execution time of functions
#     """
#     def wrapper(*args, **kw):
#         iteration_times = []
#         for _ in range(n_iter):
#             tic = time()
#             res = func(*args, **kw)
#             toc = time()
#             iteration_times.append(toc - tic)
#         avg_exec_time = mean(iteration_times)

#         print("*** Average Execution of {} :".format(func.__name__))
#         print("> The result : {}".format(res))
#         print("> Execution time : {} ms".format(avg_exec_time * 1000), end="\n\n")
#     return wrapper


class exec_time(object):
    """
    Decorator to measure te average execution time of functions.
    @Note This class doesn't start with upper case for the sake of simplicity and readbility
    """
    def __init__(self, n_iter=1):
        self.n_iter = n_iter

    def __call__(self, func):
        def wrapper(*args, **kw):
            iteration_times = []
            for _ in range(self.n_iter):
                tic = time()
                res = func(*args, **kw)
                toc = time()
                iteration_times.append(toc - tic)
            avg_exec_time = mean(iteration_times)

            print("*** Execution of {} :".format(func.__name__))
            print("> The result : {}".format(res))
            print("> Average execution time for {} iterations: {} ms".format(self.n_iter, avg_exec_time * 1000), end="\n\n")
        return wrapper
