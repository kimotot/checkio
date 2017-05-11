def checkio(n):
    if n % 3 == 0:
        flg3 = True
    else:
        flg3 = False

    if n % 5 == 0:
        flg5 = True
    else:
        flg5 = False

    if flg3 and flg5:
        return "Fizz Buzz"
    elif flg3:
        return "Fizz"
    elif flg5:
        return "Buzz"
    else:
        return str(n)


if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz"
    assert checkio(6) == "Fizz"
    assert checkio(5) == "Buzz"
    assert checkio(7) == "7"
