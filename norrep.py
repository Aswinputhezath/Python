def nonrepeat(val):
    for i in range(0,len(val)):
        num=val[i]
        if val.count(num)==1:
            print("The first non repeating letter:",num)
            break
	else:
            print("Every charcter is repeated")
val=list(input("Enter any word:"))

nonrepeat(val)
