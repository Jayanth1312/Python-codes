from functools import lru_cache
from time import perf_counter
import sys


@lru_cache(maxsize=128, typed=False)
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    sys.setrecursionlimit(10_000)

    start = perf_counter()
    f = fibonacci(1000)
    end = perf_counter()

    print(f)
    print(f'Time: {end - start} seconds')
    print(fibonacci.cache_info)