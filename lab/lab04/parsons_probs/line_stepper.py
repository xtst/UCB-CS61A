def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """

    def go(pos, r):
        # print(f"{pos} {r}")
        if pos == 0 and r == 0:
            nonlocal t
            t += 1
            # print(f"fuck {pos} {r} {t}")
            return 1
        if r < abs(pos):
            return 0

        ans = 0
        ans += go(pos + 1, r - 1)
        ans += go(pos - 1, r - 1)
        return ans

    t = 0
    # print("2: ", t)
    go(start, k)
    # print("3: ", t)
    # print(t)
    return t
    # print(t)
    # return t
