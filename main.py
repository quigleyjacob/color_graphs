import pickle
#  Need to extract all data from the .pickle files
data = open('students.pickle', 'rb')
students = pickle.load(data)
data.close()
data = open('students.pickle', 'wb')
pickle.dump(students, data)
data.close()

data = open('courses.pickle', 'rb')
courses = pickle.load(data)
data.close()
data = open('courses.pickle', 'wb')
pickle.dump(courses, data)
data.close()

data = open('edges.pickle', 'rb')
edges = pickle.load(data)
data.close()
data = open('edges.pickle', 'wb')
pickle.dump(edges, data)
data.close()

text = open('courses.txt', 'w')
i = 0
for c in courses:
    # print(str(i)+ ": " + c.toString())
    text.write(str(i)+ ": " + c.toString() + "\n")
    i+=1
text.close()
