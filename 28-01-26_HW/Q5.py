'''
prime or not prime
'''

while True :
          a = int(input("Enter a number for the beginnig interval :"))
          b= int(input("Enter a numer for the end   of interval :"))
          if b > a :
                for num in range (a , b+1):
                         if num >1 :
                              for i in range (2 , num):
                                     if num % i == 0 :
                                          print (num ,"not prime")
                                          break
                              else :
                                   print (num ,"number is prime!!!")
                         else:
                               print (num, "= number is not prime")