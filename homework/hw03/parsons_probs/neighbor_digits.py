def neighbor_digits(num, rightv_digit=-1):
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
    base = 1
    ans = 0
    while (num // base) > 0:
        now = (num // base) % 10

        if base > 1:
            right = (num // (base // 10)) % 10
        else:
            right = -1

        if num >= base * 10:
            left = (num // (base * 10)) % 10
        else:
            left = -2

        if now == right:
            ans += 1
        elif now == left:
            ans += 1
        # print(f"{base}: {left} {now} {right}")
        base *= 10
    return ans
