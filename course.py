class Course:
    def __init__(self, dept, code, sec):
        self.dept = dept
        self.code = code
        self.sec = sec
        self.students = []
        self.numStudents = 0
        self.color = 000000

    def addStudent(self, code):
        self.numStudents += 1
        self.students.append(code)

    def __eq__(self, course):
        return self.dept == course.dept and self.code == course.code

    def toString(self):
        return self.dept + " " + self.code + " " + str(self.numStudents)
