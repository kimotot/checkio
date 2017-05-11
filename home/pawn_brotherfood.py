def pawnstoxy(pawns):
    xy = set()

    for s in pawns:
        x = ord(s[0]) - ord("a")
        y = int(s[1]) - 1
        xy.add((x, y))

    return xy


def behind(x, y):
    if y == 0:
        return ()
    else:
        if x == 0:
            return ((x + 1, y - 1),)
        elif x == 7:
            return ((x - 1, y - 1),)
        else:
            return ((x + 1, y - 1), (x - 1, y - 1))


def issafe(xy, xyset):
    (x, y) = xy

    safe = False
    for b in behind(x, y):
        if b in xyset:
            safe = True

    return safe



def safe_pawns(pawns):
    xyset = pawnstoxy(pawns)
    count = 0

    for xy in xyset:
        if issafe(xy, xyset):
            count += 1

    return count


if __name__ == '__main__':

    def t():
        print(issafe((1, 0), {(0, 0), (2, 0)}))


    t()