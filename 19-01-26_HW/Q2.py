'''
קלוט מהמשתמש את הציון של דני

כעת קלוט ציונים של שאר תלמידי הכיתה
הקליטה תימשך עד שייקלט ציון שלילי או ציון גדול מ־100

לאחר סיום הקליטה
בדוק והדפס האם הציון של דני הוא הציון הגבוה ביותר בכיתה או לא
'''
maximum: int = 0
Danny  = int(input("Enter a grade for Danny: "))
while (Danny < 0) or (Danny > 100):
    Danny = int(input("Enter a new grade for Danny: "))
else :
    grade = int(input("enter a grade: "))
    while (grade >= 0) and (grade < 100):
       if  grade >= Danny:
           maximum += maximum
           grade = int(input("enter a grade: "))
       else:
            grade = int(input("enter a grade: "))
    else :
        if maximum == 0 :
         print("Danny's grade is the high grade =", Danny)

        else :
         print("maybe in the next time, Danny")

