def checkio(n):

    d = {0: ("M", "", ""),
         1: ("C", "D", "M"),
         2: ("X", "L", "C"),
         3: ("I", "V", "X")}

    def roman(n, dd):
        (c1, c5, c10) = dd
        if 0 <= n <= 3:
            return c1 * n
        elif n == 4:
            return c1 + c5
        elif 5 <= n <= 8:
            return c5 + (c1 * (n - 5))
        else:
            return c1 + c10

    st = "{0:04d}".format(n)

    ans = ""
    for idx, v in enumerate(st):
        ans += roman(int(v), d[idx])

    return ans


print(checkio(3999))