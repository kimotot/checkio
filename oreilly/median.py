def checkio(number_list):
    number_list.sort()
    length = len(number_list)
    if length % 2 == 0:
        return (number_list[length // 2] + number_list[length // 2 - 1]) / 2
    else:
        return number_list[length // 2]


if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3
    assert checkio([3, 1, 2, 5, 3]) == 3
    assert checkio([1, 300, 2, 200, 1]) == 2
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
