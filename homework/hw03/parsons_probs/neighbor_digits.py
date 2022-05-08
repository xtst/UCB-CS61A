def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    base = 10
    while num // base > 0:
        if num % base == num % (base * 10):
            ans += 1
        elif num % base == num % (base // 10):
            ans += 1
    return ans
