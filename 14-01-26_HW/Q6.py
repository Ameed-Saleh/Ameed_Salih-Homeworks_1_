'''
כתוב תוכנית בפייתון
שים בתא זיכרון pizza את מספר הפיצות שהוזמנו: 4
לכל פיצה 8 משולשים
יש במסיבה 5 אנשים
חשב באמצעות // כמה משולשים מקבל כל אורח
חשב באמצעות % כמה משולשים נשארו
'''

pizza: int  = 4
guest: int = 5
peices: int = pizza * 2
sum = pizza * peices

print ("each guest receives =" , sum // guest)
print ("the number of pizza peices left is =" ,sum % guest)

