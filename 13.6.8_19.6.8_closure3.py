import time

def timer():
    start = time.time()

    def elapsed():
        nonlocal start
        end = time.time()
        elapsed = end - start
        start = end
        return elapsed

    return elapsed