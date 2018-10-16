Year = int(input("Enter a Year to check it is a leap year or not: "))
if ((Year %4 ==0) or (Year%400 ==0)and (Year %100 != 0)):
    print("It is a leap year")
else:
   for  i in range(Year,Year+8):
    if (i %4 ==0) and (i %100 != 0) or (i%400 ==0):
        print("It is not a leap year")
        print ("the Upcomming leap year",i)
        break
 
