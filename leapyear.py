import calendar
Year = int(input("Enter the year: "))
if calendar.isleap(Year):
    print ("This is leap year")
else:
    print ("This is not leap year")
