'''
קלוט מהמשתמש:

מספר שורות
מספר עמודות
הדפס מלבן של * לפי המידות

דוגמה: אם נקלטו שורות 3 ועמודות 5 אז הפלט צריך להיות
'''
# שאלה שנייה - מלבן של כוכביות

_lines: int = int(input("Enter a number of lines: "))
_columns: int = int(input("Enter a number of columns: "))
if _lines > 0 and _columns > 0:
    for i in range(_lines):
        print("*" * _columns)
else:
    print("invalid input")


# שאלה שנייה - אופצייה שנייה
_lines: int = int(input("Enter a number of lines: "))
_columns: int = int(input("Enter a number of columns: "))
while _columns > 0 and _lines > 0 :
    a = 0
    while a < _lines:
        print("*" * _columns)
        a += 1
    else:
        _lines: int = int(input("Enter a number of lines: "))
        _columns: int = int(input("Enter a number of columns: "))
else :
    print (" No asterisk shape was received because the input is not positive!!")