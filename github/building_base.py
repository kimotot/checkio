class Building:

    def __init__(self, south, west, width_we, width_ns, height=10):
        self._south = south
        self._west = west
        self._width_we = width_we
        self._width_ns = width_ns
        self._height = height

    def corners(self):
        """corners()
        建物の角の座標の辞書を返します。 辞書は以下のキーがあります、 
        "north-west"、 "north-east"、 "south-west"、 "south-east"。 それらの値は2つの値からなるリストかタプルです。"""
        d = {}
        d["north-west"] = [self._south + self._width_ns, self._west]
        d["north-east"] = [self._south + self._width_ns, self._west + self._width_we]
        d["south-west"] = [self._south, self._west]
        d["south-east"] = [self._south, self._west + self._width_we]

        return d

    def area(self):
        return self._width_ns * self._width_we

    def volume(self):
        return self.area() * self._height

    def __repr__(self):
        """これは建物の文字列表現です。このメソッドは"print"と"str"に使われます。 以下のような形式で文字列を返します。
        "Building({south}, {west}, {width_we}, {width_ns}, {height})"""
        str = "Building({0}, {1}, {2}, {3}, {4})"
        return str.format(self._south, self._west, self._width_we, self._width_ns, self._height)


if __name__ == '__main__':
    b1 = Building(10, 10, 1, 2, 2)
    b2 = Building(0, 0, 10.5, 2.546)

    print(str(b1))
    print(str(b2))

    print(b1.corners())
    print(Building(1, 2.5, 4.2, 1.25).area())
    print(Building(1, 2.5, 4.2, 1.25, 101).volume())

