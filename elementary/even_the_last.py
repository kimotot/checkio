def checkio(li):
    s = 0
    if len(li) == 0:
        return s

    for idx, v in enumerate(li):
        if idx % 2 == 0:
            s += v
    return s * li[len(li) - 1]


if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30
    assert checkio([1, 3, 5]) == 30
    assert checkio([6]) == 36
    assert checkio([]) == 0