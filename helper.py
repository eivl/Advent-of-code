from functools import wraps
from time import perf_counter as time
import dis


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

def mod():
    return 21 % 20

def addsub():
    if 19+2 > 20:
        return 19 + 2 - 20

print(dis.dis(mod))
print(dis.dis(addsub))
