def computerScience():
    file = open("cs.txt", "r")
    lines = file.readlines()
    file.close()

    studentsCS = {line.strip( "\n" ) for line in lines}


    return studentsCS


def mathematics():
    file = open("math.txt", "r")
    lines = file.readlines()
    file.close()

    studentsMath = {line.strip( "\t\n" ) for line in lines}


    return studentsMath




studentsMath = mathematics()
studentsCS = computerScience()

print( "Students in both Computer Science and Mathematics: " )
print(studentsMath.intersection(studentsCS))
print("-" *100)
print( "Students in only Computer Science: " )
print(studentsCS - studentsMath)
print("-" *100)
print( "Students in only Mathematics: " )
print(studentsMath - studentsCS)
