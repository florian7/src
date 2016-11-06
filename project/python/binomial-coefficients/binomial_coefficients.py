coefficients = {}

def coefficient(n, k):

    if k > n or k < 0 or n < 0:
        raise ValueError("Condition not followed: 0 <= k <= n")

    if n == 0 or k == 0 or k == n:
        return 1

    if (n, k) in coefficients:
        return coefficients[(n, k)]

    c = coefficient(n - 1, k) + coefficient(n - 1, k - 1)
    coefficients[(n, k)] = c

    return c

def draw(n):
    coef_width = len(str(coefficient(n, n // 2)))

    for n_current in range(n + 1):
        line = ' ' * coef_width * (n - n_current)
        for k in range(n_current + 1):
            line += "{:^{}d}".format(coefficient(n_current, k), coef_width) + ' ' * coef_width

        print(line)
