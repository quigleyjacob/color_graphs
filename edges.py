import pickle
from course import Course
from student import Student
from edge import Edge

# the purpose of this script is to create the edges for the graph
#    using data from the .pickle file of students

data = open('./data/students.pickle', 'rb')
students = pickle.load(data)
data.close()
data = open('./data/students.pickle', 'wb')
pickle.dump(students, data)
data.close()

data = open('./data/edges.pickle', 'rb')
edgesToLoad = pickle.load(data)
data.close()

text = open('edgeHash.txt', 'w')
edges = {}
for s in students:
    courses = students[s].courses
    for c in courses:
        for d in courses:
            if c is not d:
                e = Edge(c,d)
                text.write(str(e.__hash__()) + ": " + e.toString() + "\n")
                edges[e.__hash__()] = e

text.close()

data = open('./data/edges.pickle', 'wb')
pickle.dump(edges, data)
data.close()
