import pickle
from course import Course
from student import Student
from edge import Edge

# the purpose of this script is to create the edges for the graph
#    using data from the .pickle file of students

data = open('students.pickle', 'rb')
students = pickle.load(data)
data.close()
data = open('students.pickle', 'wb')
pickle.dump(students, data)
data.close()

edges = []
for s in students:
    courses = students[s].courses
    for c in courses:
        for d in courses:
            if c is not d:
                edges.append(Edge(c,d))

data = open('edges.pickle', 'wb')
pickle.dump(edges, data)
data.close()
