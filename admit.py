# Coreen Yuen
# admission comparison tool for colleges that directly compare 2 students via inputed data by user


# introduction
def intro():
    print('This program compares two applicants to')
    print('determine which one seems like the stronger')
    print('applicant.  For each candidate I will need')
    print('either SAT or ACT scores plus a weighted GPA.')
    print()

# decimal rounding equation
def decimal(x):
    return round(x * 10.0) / 10.0

#SAT convert equation
def satConvert(math, reading, writing):
    return float(((2 * math) + reading + writing) / 32.0)

# SAT exam processing
def sat():
    math = int(input('    SAT math? '))
    reading = int(input('    SAT critical reading? '))
    writing = int(input('    SAT writing? '))
    score = satConvert(math, reading, writing)
    print('    exam score = ', decimal(score))
    return score

# ACT convert equation
def actConvert(english, math, reading, science):
    return float((english + (2 * math) + reading + science) / 1.8)

# ACT exam processing
def act():
    english = int(input('    ACT English? '))
    math = int(input('    ACT math? '))
    reading = int(input('    ACT reading? '))
    science = int(input('    ACT science? '))
    score = actConvert(english, math, reading, science)
    print('    exam score = ', decimal(score))
    return score

# exam type processing
def exam(x):
    print('Information for applicant #', str(x), ':')
    test = int(input('    do you have 1) SAT scores or 2) ACT scores? '))
    score = 0
    if (test == 1):
        score = sat()
    else:   # test == 2
        score = act()
    return score

# GPA convert equation
def gpaConvert(overall, maximum, multiplier):
    return (overall / maximum) * 100 * multiplier

# GPA processing
def gpa():
    overall = float(input('    overall GPA? '))
    maximum = float(input('    max GPA? '))
    multiplier = float(input('    Transcript Multiplier? '))
    result = gpaConvert(overall, maximum, multiplier)
    print('    GPA score = ', decimal(result))
    return result

# adds subscores of exam and GPA
def total(x):
    score = exam(x)
    result = gpa()
    print()
    return score + result;

# sum of each applicant
def report(sum1, sum2):
    print('First applicant overall score = ', decimal(sum1))
    print('Second applicant overall score = ', decimal(sum2))

# compares both applicants
def comparison(sum1, sum2):
    if (sum1 == sum2):
        print('The two applicants seem to be equal')
    elif (sum1 < sum2):
        print('The second applicant seems to be better')
    else:   # sum2 > sum1
        print('The first applicant seems to be better')

# main
intro()
sum1 = total(1)
sum2 = total(2)
report(sum1, sum2)
comparison(sum1, sum2)
