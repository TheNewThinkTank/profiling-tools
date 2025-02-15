"""
Deterministic profiling of Python programs using cProfile as decorator.
"""

import cProfile
import functools
import os


def profile(func):
    """Decorator for profiling a function using cProfile."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)  # Execute the wrapped function
        profiler.disable()

        # Ensure the 'stats' directory exists
        stats_dir = "stats"
        if not os.path.exists(stats_dir):
            os.makedirs(stats_dir)

        # Save the profiling stats with the function's name
        stats_file = f"{stats_dir}/{func.__name__}.stats"
        profiler.dump_stats(stats_file)

        return result
    return wrapper
