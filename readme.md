# Graph Coloring for scheduling final exams for numCourses

The general organization for this repo is as follows:
* The singular of a word is the object file for that word
* The plural file is a script that extracts data from a .xlsx file and moves it to a pickle file (those are ignored in this repo, but the scripts can be altered minimally to fit any such file)

And then, the main file is the script to take all extracted data and color the graph, hopefully finding an optimal solution to the problem of scheduling final exams without conflicts (optimization being the least amount of days needed for finals)
