class Friends:

    def __init__(self, connections):
        self._connections = list(connections)


    def add(self, connection):
        if connection in self._connections:
            return False
        else:
            self._connections.append(connection)
            return True


    def remove(self, connection):
        if connection in self._connections:
            self._connections.remove(connection)
            return True
        else:
            return False


    def names(self):
        ret = set()
        for connection in self._connections:
            for p in connection:
                ret.add(p)
        return ret


    def connected(self, name):
        ret = set()
        for connection in self._connections:
            if name in connection:
                for p in connection:
                    ret.add(p)

        if name in ret:
            ret.remove(name)

        return ret
