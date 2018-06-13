class Edge:
    def __init__(self, c1, c2):
        self.courses = set([c1, c2])

    def __eq__(self, e):
        return self.courses == e.courses
