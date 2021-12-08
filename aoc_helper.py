from functools import wraps
from time import perf_counter as time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = time() - start
            print(f"Exe-time of {func.__name__}: {end_ if end_ > 0 else 0} "
                  f"sec")
    return _time_it
