'''
קלוט מספרים מהמשתמש
הקליטה תימשך עד אשר ייקלטו שני מספרים זהים ברצף
רמז:
בכל שלב יש לזכור את המספר האחרון שנקלט
כאשר מתקיים התנאי – סיים את התוכנית
'''

b = None
a = float(input("press a number:"))
while a != b :
    b = a
    a = float(input("press another number:"))
else :
    print("there is two nembers in a while!")