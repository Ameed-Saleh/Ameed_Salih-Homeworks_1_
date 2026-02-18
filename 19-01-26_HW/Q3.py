'''
בכל חדר במלון יכולים לשהות 4 אנשים
קלוט מהמשתמש את מספר האנשים בקבוצה
חשב והדפס:
כמה חדרים יהיו מלאים
האם קיים חדר שאינו מלא
אם כן – כמה אנשים יהיו בחדר שאינו מלא
'''
people: int = int(input("How many people are you? "))
if people % 4 == 0:
    print ("there will be ", people // 4, "full room exactly")
else :
    print ("there will be ", people // 4, "full rooms and one room of", people % 4)