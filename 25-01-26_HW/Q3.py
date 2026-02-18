'''
כתוב תוכנית שקולטת מספר שלם ומדפיסה אם הוא ראשוני או לא

תזכורת: מספר ראשוני מתחלק רק ב־1 ובעצמו דוגמאות למספרים ראשוניים: 2, 3, 5, 7, 11, 13, 17, 19, 23

אלגוריתם מומלץ:

אם המספר קטן או שווה ל־1 – הוא לא ראשוני
אחרת, בדוק בלולאה מחלקים מ־2 ועד המספר (לא כולל המספר)
אם מצאת מחלק בלי שארית – הוא לא ראשוני
אם לא מצאת אף מחלק – הוא ראשוני
'''

# שאלה 3 - אתגר מספר ראשוני

number = 2
a: int = int(input("a: "))
while a % number != 0:
    number += 1
else:
    if a == number:
        print("the number" , a ,  "is prime")
    else:
        print("a is not prime")

# אופצייה שנייה

num = 2
number: int = int(input("Enter a number: "))
if number <= 1:
   print("המספר הוא לא ראשוני!")
else:
    while number % num != 0:
        num += 1
    else:
        if number == num:
            print("the number" , number,  "is prime!!")
        else:
            print(number ," is not prime")

