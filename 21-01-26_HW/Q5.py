'''
קלוט מהמשתמש את מספר התלמידים בכיתה

כעת קלוט את הציון של כל תלמיד בלולאה
ציון שאינו בין 0 ל־100 – יש להתעלם ממנו ולא להתקדם לתלמיד הבא

לאחר שנקלטו ציונים תקינים עבור כל התלמידים
חשב והדפס את ממוצע הציונים
'''

# שאלה 5 – ציונים בכיתה

# a = 0
# sum =0
# students: int = int(input("enter the number of students: "))
# while a < students:
#     grade = int(input("enter the grade: "))
#     if grade > 100 or grade < 0:
#         print("grade is out of range")
#     else:
#         sum = sum + grade
#         a += 1
# print("ממוצע הציונים של תלמידי הכיתה הוא:", sum/students)


_num_students: int = int(input("enter number of students: "))
current_students: int = 0
_sum: int = 0
while current_students < _num_students:
    grade: int = int(input("enter grade: "))
    while grade < 0 or grade > 100:
        grade = int(input("enter grade: "))

    _sum += grade
    current_students += 1

_avg = _sum / _num_students
print ("avg", _avg)
