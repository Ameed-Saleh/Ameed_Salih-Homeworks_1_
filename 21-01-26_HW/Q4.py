'''
יש 10 סרטים שצריך לדרג
קלוט מהמשתמש דירוגים (מספרים שלמים) בין 1 ל־5

המשך לקלוט עד שהתקבלו דירוגים תקינים עבור כל 10 הסרטים
דירוג שלא בין 1 ל־5 – יש להתעלם ממנו ולא לספור אותו

בסיום הדפס את ציון הסרט הכי גבוה ואת ציון הסרט הכי נמוך מתוך 10 הסרטים שנקלטו
'''
# שאלה 4 – דירוג 10 סרטים

maximum = 0
minimum = None
i = 1
films = int(input("enter the number of films: "))
while i <= films:
    rating: int = int(input("enter a rating for film: "))
    if rating > 5 or rating < 1:
        print("rating is out of range, try again")
    else :
        if  minimum is None or rating < minimum :
          minimum = rating
          i += 1
        else:
            if  rating > maximum:
              maximum = rating
              i += 1

            else:
              i += 1
else:
  print("number of films is:", films)
  print("the lowest film rating is:", minimum)
  print("the highest film rating is:", maximum)

# min: int = 0
# max: int = 0
# movies: int = 0
# while movies <= 4:
#     rating: int = int(input("enter your rating for movies:"))
#     while rating < 1 or rating > 5:
#         print("rating must be between 1 and 5")
#         rating: int = int(input("enter your rating for movies:"))
#     if movies == 0:
#         min = max = rating
#     else:
#         if rating > max:
#            max = rating
#         if rating < min:
#            min = rating
#     movies += 1
#
# print(min,max)
# print(movies)
# print ()
