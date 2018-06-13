import os, sys
import pickle
from course import Course

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

data = xlsx(filename)
courses = []
dumpFile = open('courses.pickle', 'wb')
for d in data:
    course = Course(d['A'], d['B'], d['C'])
    currentCourse = courses[-1] if len(courses) > 0 else Course(None, None, None)
    if not course.__eq__(currentCourse):
        courses.append(course)
    courses[-1].addStudent(d['H'])

pickle.dump(courses, dumpFile)
dumpFile.close()
