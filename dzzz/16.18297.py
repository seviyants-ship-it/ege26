from functools import lru_cache

def f(n):
    if n < 10: return (n - 1)
@lru_cache(None)
def f(n):
    if n >= 10: return 3 * n - 1 + f(n - 3)
def f(n):
    if n >= 10, return 5 * n + 2 + f(n - 4)
for i in range(9,5000)[::-1]:

print(f(4445) - (4444))