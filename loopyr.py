Year = int(input("Enter a Year to check it is a leap year or not: "))
if ((Year %4 ==0) or (Year%400 ==0)and (Year %100 != 0)):
    print("It is a leap year")
else:
    print("It is not leap year")
