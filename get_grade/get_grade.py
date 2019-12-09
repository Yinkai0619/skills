#!/usr/bin/env python3

import bisect

def get_grade(score):
    break_points = [60, 70, 80, 90]
    grades = 'EDCBA'
    return grades[bisect.bisect(break_points, score)]

if __name__ == "__main__":
    print(get_grade(100))