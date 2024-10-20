def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Function {func.__name__} raised an exception: {e}")
    return wrapper