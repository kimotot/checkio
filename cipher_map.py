def key2yx(key):
    ans = []
    for y , xstr in enumerate(key):
        for x, c in enumerate(xstr):
            if c == "X":
                ans.append((y, x))
    return ans


def yxrotate(yx):
    ans = []
    for y, x in yx:
        ans.append((x, 3 - y))
    ans.sort(key = lambda x: x[1])
    ans.sort(key = lambda x: x[0])

    return ans


def cryptread(yx, alp):
    ans = ""
    for y, x in yx:
        ans += alp[y][x]
    return ans


def recall_password(key, alp):
    yx = key2yx(key)
    pas = ""

    for _ in range(4):
        pas += cryptread(yx, alp)
        yx = yxrotate(yx)

    print(pas)


if __name__ == '__main__':

    def t():
        recall_password(
            ('....',
             'X..X',
             '.X..',
             '...X'),
            ('xhwc',
             'rsqx',
             'xqzz',
             'fyzr'))

    def t2():
        key =('X...',
             '..X.',
             'X..X',
             '....')
        yx = key2yx(key)
        print(yx)

        yx = yxrotate(yx)
        print(yx)


    t()