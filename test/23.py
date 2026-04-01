def f(current,end):
    if current == end: return 1
    if current < end or current
    return f(current - 1) + f(current // 2,end)
