def left_join(t):
    ans = []
    for word in t:
        ans.append(word.replace("right", "left"))

    return ",".join(ans)


if __name__ == '__main__':
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
    assert left_join(("brightness wright",)) == "bleftness wleft"
    assert left_join(("enough", "jokes")) == "enough,jokes"