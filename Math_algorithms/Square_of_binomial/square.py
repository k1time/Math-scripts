# The method of allocating the square of a binomial

def complete_the_square(a, b, c):
    if a != 1:
        a = 1
        b /= a
        c /= a
    
    b = b / 2
    squared_b_power = b ** 2
    c = c - squared_b_power

    if b < 0:
        result = f"(x - {b})^2 = {c}"
    else:
        result = f"(x + {b})^2 = {c}"

    return result
