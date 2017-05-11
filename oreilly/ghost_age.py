def fibo(max_n):
    fibo_list = [0, 1]

    n = 2
    v = 1

    while v <= max_n:
        fibo_list.append(v)
        n += 1
        v = fibo_list[n - 1] + fibo_list[n - 2]

    return fibo_list


def opa(flist):
    y = 0
    o = 10000
    d = {}

    while y < 5000:
        d[o] = y
        y += 1
        if y in flist:
            o = o - y
        else:
            o += 1

    return d


def checkio(n):
    flist = fibo(5000)
    d = opa(flist)
    return d[n]


if __name__ == '__main__':
    flist = fibo(5000)
    d = opa(flist)
    for key, v in d.items():
        print(key, v)