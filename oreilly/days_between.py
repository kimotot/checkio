import datetime

def days_diff(t1, t2):
    date1 = datetime.date(t1[0], t1[1], t1[2])
    date2 = datetime.date(t2[0], t2[1], t2[2])

    delta = date2 - date1

    return abs(delta).days


if __name__ == '__main__':
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
