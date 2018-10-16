R = int(input("Enter the range for fibonacci \n"))
R = R + 1
a = 1
b = 0
c = 0
for i in range (1, (R)):
        print (a)
        c = a
        a = a+b
        b = c
