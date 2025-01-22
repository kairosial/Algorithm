record = {}
grade_dict = {'A+':4.5,
              'A0':4.0,
              'B+':3.5,
              'B0':3.0,
              'C+':2.5,
              'C0':2.0,
              'D+':1.5,
              'D0':1.0,
              'F':0.0}

for i in range(20):
    course, credit, grade = input().split()
    if grade == 'P':
        continue
    credit = float(credit)
    grade = grade_dict[grade]
    record[course] = [credit, grade]

gpa = 0
total_sum = 0
total_credit = 0

for credit, grade in list(record.values()):
    total_sum += credit * grade
    total_credit += credit

gpa = total_sum / total_credit
print(gpa)