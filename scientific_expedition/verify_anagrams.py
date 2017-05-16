def verify_anagrams(stra, strb):

    def strtodic(arg):
        d = {}
        str = arg.lower()
        str = str.replace(" ", "")
        for c in str:
            d[c] = d.get(c, 0) + 1
        return d

    if strtodic(stra) == strtodic(strb):
        return True
    else:
        return False


if __name__ == '__main__':
    assert verify_anagrams("Programming", "Gram Ring Mop") == True
    assert verify_anagrams("Hello", "Ole Oh") == False
    assert verify_anagrams("Kyoto", "Tokyo") == True
