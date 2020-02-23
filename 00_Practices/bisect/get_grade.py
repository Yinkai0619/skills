import bisect

def get_grade(score):
    breakpoints = [60, 70, 80, 90]
    grades = 'EDCBA'
    return grades[bisect.bisect(breakpoints, score)]

print(get_grade(100))