'''
משולש שווה שוקיים הוא משולש שבו שתי צלעות שוות
משולש שווה צלעות הוא משולש שבו כל שלוש הצלעות שוות

קלוט מהמשתמש שלוש צלעות של משולש

הדפס:

"משולש שווה צלעות" אם כל הצלעות שוות
"משולש שווה שוקיים" אם רק שתי צלעות שוות
"אינו משולש מיוחד" אם אינו אחד מהמקרים
'''

# a = float(input("Enter a number: "))
# b = float(input("Enter a number: "))
# c = float(input("Enter a number: "))
# if a == b == c :
#     print("משולש שווה צלעות")
# elif a == b:
#     print("משולש שווה שוקיים")
# elif a == c:
#     print("משולש שווה שוקיים")
# elif b == c:
#     print("משולש שווה שוקיים")
# else:
#     print("אינו משןלש מיוחד לצערי הרב")


a = float(input("Enter a slide 1: "))
b = float(input("Enter a slide 2: "))
c = float(input("Enter a slide 3: "))
if a == b == c :
    print("משולש שווה צלעות")
else :
    if a == b or a == c or b == c:
      print("משולש שווה שוקיים")
    else:
      print("אינו משןלש מיוחד לצערי הרב")

