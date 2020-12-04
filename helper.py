from functools import wraps
from time import perf_counter as time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            # end_ = int(round(time() * 1000)) - start
            end_ = time() - start
            print(f"Exe-time of {func.__name__}: {end_} ms")
    return _time_it


def validate_hair_colour(hair_colour):
    """Validate if the passport has valid hair colour"""
    return False if (hair_colour[0] != '#' or len(hair_colour) != 7) else True

print(validate_hair_colour('#d345abc'))