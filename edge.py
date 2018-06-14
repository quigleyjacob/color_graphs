class Edge:
    def __init__(self, c1, c2):
        self.courses = frozenset([c1, c2])

    def __eq__(self, e):
        return self.courses == e.courses

    def __hash__(self):
        code = 1
        for c in self.courses:
            code *= c.__hash__()
        return code

    def toString(self):
        str = ""
        for c in self.courses:
            str += c.toString() + ","
        return str
