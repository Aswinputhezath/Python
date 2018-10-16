def factorial():
    fact = 1
    if ipnum < 0:
        return("Not applicable for negative number")
    elif ipnum == 0:
        return("1")
    else:
        for i in range(1,ipnum+1):
            fact = fact*i
        return(fact)
ipnum = int(input("Enter the number: "))
print (factorial())
