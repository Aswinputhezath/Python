def nonrepstring(str):
  for i in range(len(str)):
    cnt=str[i]
    if str.count(cnt)==1:
      return("non repeating character is",cnt)
      break
  else:
    return("All characters are repeating")


       


    
        

