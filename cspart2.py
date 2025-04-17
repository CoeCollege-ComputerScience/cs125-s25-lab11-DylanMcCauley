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

def studentYear(studentsCS, studentsMath):
    file = open("studentYear.txt", "r")
    lines = file.readlines()
    file.close()

    studentsYear = {line.strip("\t\n") for line in lines}
    sophomoreCS = {line.split (",")[1] for line in lines if line.startswith("2")}.intersection(studentsCS)
    freshmenNotMathOrCS = {line.split(",")[1] for line in lines if line.startswith("1")}.difference(studentsMath.union(studentsCS))
    seniorMathAndCS = {line.split(", ")[1] for line in lines if line.startswith("4")}.intersection(studentsMath.union(studentsCS))

    return studentsYear, sophomoreCS, freshmenNotMathOrCS, seniorMathAndCS


studentsMath = mathematics()
studentsCS = computerScience()
studentsYear = studentYear(studentsCS, studentsMath)

