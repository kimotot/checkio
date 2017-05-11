import functools

def checkio(num):

    num_list = [int(c) for c in str(num).replace("0", "")]
    return functools.reduce(lambda x, y: x * y, num_list)


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1