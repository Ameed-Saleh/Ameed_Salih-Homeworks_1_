'''
קלוט מהמשתמש מספר שלם
אם המספר זוגי – הדפס even
אחרת – הדפס odd

הערה: יש להשתמש בהמרה ל־int, לדוגמה: number = int(input('enter number? '))
'''

# שאלה 1 – זוגי או אי־זוגי

number: int = int(input("enter a number? "))
if number % 2 == 0:
#YES
    print("number is even", number)
else :
#NO
    print("number is odd",number)