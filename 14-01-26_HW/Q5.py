'''
כתוב תוכנית בפייתון המציבה בתא זיכרון width את הערך 30
ובתא זיכרון height את הערך 40
אלו האורך והרוחב של מלבן
חשב את שטח המלבן לתוך תא זיכרון area
חשב את היקף המלבן לתוך תא זיכרון perimeter
הדפס את השטח וההיקף שחישבת
'''

width: int = 30
height: int = 40
area = width * height
perimeter = 2 * (width + height)
print("area = ", area )
print("perimeter = ", perimeter)

