from functools import wraps
from time import perf_counter

def memorize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


class Solution:
    @memorize
    def reverse(self, x: int) -> int:
        if x<0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        
        rev_int = 0
        while x!=0:
            digit = x%10
            rev_int = rev_int * 10 + digit
            x //= 10

        if rev_int > 2**31 - 1 or rev_int < -2**31:
            return 0

        return sign*rev_int
    
if __name__ == '__main__':
    start = perf_counter()
    s = Solution()
    r = s.reverse(-12313641)
    end = perf_counter()

    print(r)
    print(f'time: {end-start} seconds')