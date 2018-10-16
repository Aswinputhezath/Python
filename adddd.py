num = {30:'a',1:'r',20:'a',100:7,4:4,15:'jj',50:'i'}
print("Before updating value to key:\n",num)
num.update({30:'z'})
print("After adding new value to existing key 30:\n",num)
num.update({20:'over'})
num1={10:'done'}
num.update(num1)
print("Added new keys and values:\n",num)
