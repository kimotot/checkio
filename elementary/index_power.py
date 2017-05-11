def index_power(li, n):
    if len(li) <= n:
        return -1
    else:
        return li[n] ** n


if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9
    assert index_power([1, 3, 10, 100], 3) == 1000000
    assert index_power([0, 1], 0) == 1
    assert index_power([1, 2], 3) == -1