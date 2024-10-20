import time

def time_it(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function {func.__name__} took {int(end - start)} seconds to run")
    return wrapper