from edge import Edge

class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e

    def run(self):
        matrix = ""
        for v in self.v:
            for n in self.v:
                if v is not n:
                    nv = Edge(n,v)
                    matrix += "1" if nv.__hash__() in self.e else "0"
            matrix+="\n"
        text = open('./data/matrix.txt', 'w')
        text.write(matrix)
        text.close()
