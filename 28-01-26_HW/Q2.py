'''
כתוב תוכנית שקולטת שני מספרים מהמשתמש:
קלוט lower – מספר נמוך higher – מספר גבוה
כללים:
יש לקלוט את lower לאחר מכן, יש לקלוט את higher בלולאת while True
אם higher קטן או שווה ל־lower – יש להמשיך לקלוט שוב 2 ערכים
כאשר higher גדול מ־lower – יוצאים מהלולאה ב break
לבסוף, הדפס את כל המספרים מ־lower עד higher (כולל) באמצעות for עם range
'''

_lower = int(input("the lower limit: "))
while True:
   _higher = int(input("the higher limit: "))
   if  _higher > _lower:
       print("🔉"," ~~lower~~ = ", _lower)
       print("🔊"," ~~higher~~ = ", _higher)
       break
   if _higher <= _lower:
       _lower = int(input("the lower limit: "))
       continue
for _ in range(_lower, _higher +1 ):
    print( _ , end="  ")
