import time, math


coefficients = {}


def coefficient(n, k):
    return coefficient_recursive(n, k)


def coefficient_recursive(n, k):

    if k > n or k < 0 or n < 0:
        raise ValueError("Condition not followed: 0 <= k <= n")

    if n == 0 or k == 0 or k == n:
        return 1

    if (n, k) in coefficients:
        return coefficients[(n, k)]

    c = coefficient_recursive(n - 1, k) + coefficient_recursive(n - 1, k - 1)
    coefficients[(n, k)] = c

    return c


def coefficient_factorial(n, k):

    if k > n or k < 0 or n < 0:
        raise ValueError("Condition not followed: 0 <= k <= n")

    return math.factorial(n) // math.factorial(n - k) // math.factorial(k)

def draw(n):
    coef_width = len(str(coefficient(n, n // 2)))

    for n_current in range(n + 1):
        line = ' ' * coef_width * (n - n_current)
        for k in range(n_current + 1):
            line += "{:^{}d}".format(coefficient(n_current, k), coef_width) + ' ' * coef_width

        print(line)

def test(n):
    
    print(" n    | t_recursive  | t_factorial  ")
    print("======+==============+==============")

    for n_current in range(n + 1):
            
        t0 = time.time()
            
        for k in range(n_current + 1):
            coefficient_recursive(n_current, k)
                
        t1 = time.time()

        for k in range(n_current + 1):
            coefficient_factorial(n_current, k)

        t2 = time.time()


        t_recursive = (t1 - t0) / (n + 1)
        t_factorial = (t2 - t1) / (n + 1)

        print(" {:4d} | {:12f} | {:12f}".format(n_current, t_recursive, t_factorial))
