
def log(func):
    '''print log'''
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Successfully run the func {func.__name__}.\n")
            return result
        except Exception as e:
            print(f"Something wrong with func {func.__name__}: {e}\n")

    return wrapper