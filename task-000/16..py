from functools import lru_cache

def f(n):
if n >=2025: return

@lru_cache(None)
def f(n):
    if n < 2025: return (n + 1)