# print את לוח הכפל, 1*3 2*1 1*1 3*10 2*10 3*10

x: int = 1
y: int = 1
while x <= 10:
    while y < 10:
        print(x ,"*", y  , end="\t")
        y += 1

    print(x ,"*", y )
    x += 1
    y = 1