print("---Reverse dictionary lookup---")
def reverseLookup(d,value):
    keys = [k for k,v in d.items() if v==value]
    return keys
dict={1:"c",2:"b",3:"c",4:"d",5:"c"}
value_to_find="c"
result=reverseLookup(dict,value_to_find)
print("Keys with value",value_to_find,":",result)