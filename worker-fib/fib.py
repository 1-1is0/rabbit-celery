
def fib_calc(a:int) -> int:
    if  a <= 1:
        return 0
    elif a == 2:
        return 1
    else:
        return fib_calc(a-1) + fib_calc(a-2)
