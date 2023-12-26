import time

def log(func):
    '''print log'''
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Successfully run the func {func.__name__}.\n")
            return result
        except Exception as e:
            print(f"log wrong with func {func.__name__}: {e}\n")

    return wrapper

def time_count(func):
    '''time ms'''
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            dur_time = end_time - start_time
            print(f"Finished process, use {dur_time:.2f} s\n")
            return result
        except Exception as e:
            print(f"time_count wrong with func {func.__name__}: {e}\n")

    return wrapper
            