import functools

def checkio(str_number, radix):
    number_list = []
    for c in str_number:
        if c.isdigit():
            number_list.append(int(c))
        else:
            number_list.append(ord(c) - ord("A") + 10)

    if functools.reduce(lambda x, y: x and y, map(lambda x: x < radix, number_list)):
        ans = 0
        for i in number_list:
            ans = ans * radix + i
        return ans
    else:
        return -1


if __name__ == '__main__':
    assert checkio("AF", 16) == 175
    assert checkio("101", 2) == 5
    assert checkio("101", 5) == 26
    assert checkio("Z", 36) == 35
    assert checkio("AB", 10) == -1