'''
קלוט מהמשתמש מספר שלם
בדוק לפי הסדר:

אם המספר מתחלק ב־2 ללא שארית – הדפס 2
אחרת, אם המספר מתחלק ב־3 ללא שארית – הדפס 3
אחרת, אם המספר מתחלק ב־5 ללא שארית – הדפס 5
אחרת – הדפס no small dividers
'''

#שאלה 2 – מחלקים קטנים

w: int = int(input("Enter a number: "))
if w % 2 == 0:
    #YES
    print( "the number divides by:" ,2 )
elif w % 3 == 0:
    print( "the number divides by:", 3 )
elif w % 5 == 0:
    print("the number divides by:", 5)
else:
    #NO
    print(" no small dividers ")
