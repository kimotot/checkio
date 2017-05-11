def find_message(s):
    message = list(filter(lambda c: c.isupper(), s))
    return "".join(message)


if __name__ == '__main__':

    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    assert find_message("hello world!") == ""