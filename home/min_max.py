def comparison(*args, **kwargs):
    key = kwargs.get("key", None)
    f = kwargs.get("func", None)

    if len(args) == 1:
        it = args[0]
    else:
        it = args

    result = None

    if key is None:
        for i in it:
            if result is None:
                result = i
            else:
                if f(result, i):
                    pass
                else:
                    result = i
        return result
    else:
        for i in it:
            if result is None:
                result = i
            else:
                if f(key(result), key(i)):
                    pass
                else:
                    result = i
        return result


def max(*args, **kwargs):
    kwargs["func"] = lambda a, b: a >= b
    return comparison(*args, **kwargs)


def min(*args, **kwargs):
    kwargs["func"] = lambda a, b: a <= b
    return comparison(*args, **kwargs)


if __name__ == '__main__':

    print(min(abs(i) for i in range(-10, 10)))