'''
קלוט מהמשתמש ציון (מספר שלם)

כללים:

אם הציון גדול מ־100 או קטן מ־0 – הדפס invalid
אחרת, אם הציון בין 80 ל־100 (כולל) – הדפס VERY GOOD
אחרת, אם הציון בין 60 ל־80 (כולל 60, לא כולל 80) – הדפס NOT BAD
אחרת, אם הציון בין 40 ל־60 (כולל 40, לא כולל 60) – הדפס TRY HARDER
אחרת, אם הציון בין 0 ל־40 (כולל) – הדפס NEED MORE EXERCISE
הערה: יש להשתמש ב־if / elif / else
'''
# שאלה ראשנה - דירוג ציון
# if-elif-else_Question

grade: int = int(input("Enter a grade: "))
if grade > 100 or grade < 0:
    print("Invalid Grade")
elif grade >= 80 :
    print("Your Grade is Very Good !! ")
elif grade >= 60:
    print("Your Grade is Not Bad !! ")
elif grade >= 40:
    print("Your Grade is Bad !! ")
else :
    print ("Invalid Grade =", grade)

# שאלה 1- אופצייה שנייה
grade: int = int(input("Enter a grade: "))
while grade > 100 or grade < 0 :
    print(grade ," = invalid geade!")
    grade: int = int(input("Please enter another grade: "))
else:
    if grade >= 80:
       print("Your Grade is Very Good !! ")
    elif grade >= 60:
       print("Your Grade is Not Bad !! ")
    elif grade >= 40:
       print("Your Grade is Bad Try Harder !! ")
    elif grade >= 0:
       print("Your Grade is Relly Bad , You Need More Exercise!! ")