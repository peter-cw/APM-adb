from functools import wraps
import time
def keyword(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        ts_start = time.time()
        res =func(*args,**kwargs)
        ts_end = time.time()
        print('%r execute takes %r'%('.'+func.__name__,ts_end-ts_start))
        return res
    return wrapper

