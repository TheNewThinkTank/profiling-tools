"""
usage (simple decorators):
decorate functions with: @simple_timer, @debug, @memoize

usage (parameterized decorators / decorator factory):
decorate functions with: @timer, or @timer("ms", precision=3)
"""

import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

UNITS = ("ns", "us", "ms", "s")

P = ParamSpec("P")
R = TypeVar("R")


def simple_timer(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result
    return wrapper


def timer(unit: str = "ns", *, precision: int = 0) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time.perf_counter_ns()
            result = func(*args, **kwargs)
            delta = (time.perf_counter_ns() - start) / (1_000 ** UNITS.index(unit))
            print(f"{func.__name__} took {delta:,.{precision}f} {unit}")
            return result
        return wrapper
    return decorator


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper
