import pickle
from graph import Graph
from course import Course
from edge import Edge
#  Need to extract all data from the .pickle files
data = open('./data/students.pickle', 'rb')
students = pickle.load(data)
data.close()
data = open('./data/students.pickle', 'wb')
pickle.dump(students, data)
data.close()
#
data = open('./data/courses.pickle', 'rb')
courses = pickle.load(data)
data.close()
data = open('./data/courses.pickle', 'wb')
pickle.dump(courses, data)
data.close()
#
data = open('./data/edges.pickle', 'rb')
edges = pickle.load(data)
data.close()
data = open('./data/edges.pickle', 'wb')
pickle.dump(edges, data)
data.close()

g = Graph(courses, edges)
g.run()
