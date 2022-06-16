from curses.ascii import FF


def remove_odd_indices(lst, odd):
    """
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """

    def letin(index):
        if index % 2 == 0:
            if odd:
                return True
            return False
        if index % 2 == 1:
            if not odd:
                return True
            return False

    ans = []
    for i in range(0, len(lst)):
        if letin(i):
            ans.append(lst[i])
    return ans
