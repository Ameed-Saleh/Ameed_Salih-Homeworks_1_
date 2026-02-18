# 1
# input numbers of classes
# print numbers 1.....classes
a = 1
classes: int = int(input('Enter classes: '))
while classes != a:
    print ("class", a)
    a += 1

# 2
# #input number of students, input grades for all students, print avg
k = 0
sum = 0
num_student: int = int(input("Enter a number of students: "))
while k <= num_student:
    grade: int = int(input("Enter a grade: "))
    sum += grade
    k += 1
else:
    print("avg=", sum / num_student)


# 4
# לולא מקוננתת שילוב של שתי השאלות 2 +  3
# nested_loops3 + nested_loops4

a = 1
classes: int = int(input('Enter classes: '))
while classes != a:
    print ("class", a)
    k = 0
    _sum = 0
    num_student: int = int(input("Enter a number of students: "))
    while k <= num_student:
        grade: int = int(input("Enter a grade: "))
        _sum += grade
        k += 1
    else:
        print("avg=", _sum / num_student)
        a += 1
else:
    print("finished all classes!!")