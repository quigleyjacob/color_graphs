import os, sys
import pickle
from student import Student
from course import Course

#  This file is used to take in the information from the final exam schedule
#  and create student objects, who are assigned a key code, and they have
#  stored the classes that they have finals in

filename = sys.argv[1]

def xlsx(fname):
    import zipfile
    from xml.etree.ElementTree import iterparse
    z = zipfile.ZipFile(fname)
    strings = [el.text for e, el in iterparse(z.open('xl/sharedStrings.xml')) if el.tag.endswith('}t')]
    rows = []
    row = {}
    value = ''
    for e, el in iterparse(z.open('xl/worksheets/sheet1.xml')):
        if el.tag.endswith('}v'): # <v>84</v>
            value = el.text
        if el.tag.endswith('}c'): # <c r="A3" t="s"><v>84</v></c>
            if el.attrib.get('t') == 's':
                value = strings[int(value)]
            letter = el.attrib['r'] # AZ22
            while letter[-1].isdigit():
                letter = letter[:-1]
            row[letter] = value
            value = ''
        if el.tag.endswith('}row'):
            rows.append(row)
            row = {}
    return rows

students = {}
data = xlsx(filename)

dumpFile = open('students.pickle', 'wb')
for d in data:
    course = Course(d['A'], d['B'], d['C'])
    if d['H'] not in students:
        students[d['H']] = Student(d['H'])
    students[d['H']].addCourse(course)
    students[d['H']].numCourses += 1

print(students)
for s in students:
    print(students[s].toString())
pickle.dump(students, dumpFile)
dumpFile.close()
