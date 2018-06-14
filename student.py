class Student:
    def __init__(self, code):
        self.code = code
        self.courses = []
        self.numCourses = 0

    def addCourse(self, c):
        self.courses.append(c)

    def __eq__(self, s):
        return self.code == s.code

    def toString(self):
        return str(self.code) + " " + str(self.numCourses)
