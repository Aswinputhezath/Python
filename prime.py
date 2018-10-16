value = int(input("Enter a number: "))
if (value < 1):
   print("this is a negative number")
elif (value == 1):
   print("this is not a prime number")
   
if (value>1):
   for i in range(2,value):
      if (value % i) == 0:
         print("This is not a prime number")
         break
   else:
      print("This a prime number")  

