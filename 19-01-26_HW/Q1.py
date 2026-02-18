'''
שטח משולש מחושב כך:
גובה × בסיס ÷ 2

קלוט מהמשתמש גובה
אם הגובה אינו מספר חיובי – המשך לקלוט עד שייקלט מספר חיובי

קלוט מהמשתמש בסיס
אם הבסיס אינו מספר חיובי – המשך לקלוט עד שייקלט מספר חיובי

חשב והדפס את שטח המשולש
'''

# height = float(input('Enter height: '))
# while  height <= 0:
#     height = float(input('Enter height: '))
# base = float(input('Enter base: '))
# while base <= 0:
#      base = float(input('Enter base: '))
# print("area =", (base * height)/2 )


base = float(input('Enter base: '))
height = float(input('Enter height: '))
while base <= 0 or height <= 0:

    if base > 0 :
        base = base
    else:
        base = float(input('Enter base: '))
    if height > 0 :
        height = height
    else:
        height = float(input('Enter height: '))

else :
    print("area =", (base * height)/2 )