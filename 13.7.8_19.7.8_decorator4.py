import random

def ensure_result_is_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return result
        else:
            return None
    return wrapper