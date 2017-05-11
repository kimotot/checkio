def checkio(s):

    count = 0
    for word in s.split(" "):
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0

    return False


if __name__ == '__main__':
    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("bla bla bla bla") == True
    assert checkio("Hi") == False