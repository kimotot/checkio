def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return None


if __name__ == '__main__':

    min([1,2,3], key=lambda x: x[1])