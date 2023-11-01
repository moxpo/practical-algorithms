import random
import sys
import time

studentList = []
studentDict = {}

def makeList(numberOfStudents):
    for i in range(numberOfStudents):
        grade1 = random.randint(1, 100)
        grade2 = random.randint(1, 100)
        grade3 = random.randint(1, 100)
        studentList.append((i, round((grade1+grade2+grade3)/3)))
    return studentList

def makeDictonary(numberOfStudents):
    for i in range(numberOfStudents):
        grade1 = random.randint(1, 99)
        grade2 = random.randint(1, 99)
        grade3 = random.randint(1, 99)
        studentDict.update({i:round((grade1+grade2+grade3)/3)})
    return studentDict


startListTime = time.time()
makeList(1000)
endListTime = time.time()
totalListTime = endListTime-startListTime

startDictTime = time.time()
makeDictonary(1000)
endDictTime = time.time()
totalDictTime = endDictTime-startDictTime




print("total list time " + str(totalListTime) + " with a size of " + str(sys.getsizeof(studentList)))
print("total dict time " + str(totalDictTime) + " with a size of " + str(sys.getsizeof(studentDict)))



"""
Student comments :
    Dictionary has a much larger size with a slight longer time to complete
"""




"""

5a) Find the average of marks in 3 subjects for a 1000 students. The students' id range from 0 to 999. The marks 
can be generated randomly. Implement this using both lists and dictionaries. Compare the size (of the data structures) 
in memory as well as performance (ie, running time), and comment on your findings.

"""