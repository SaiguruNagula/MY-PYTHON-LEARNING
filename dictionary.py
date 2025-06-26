# dictionary =  a collection of {key:value} pair , 
#               ordered and changeable,
#               allows duplicate members

capitals = {"India": "New Delhi","USA": "Washington DC", "Japan": "Tokyo", "China": "Beijing", "Russia": "Moscow"}

print(capitals)


#print(dir(capitals))
#print(help(capitals))

print(capitals.get("India"))
cap= input("Enter the country name: ").upper()



if capitals.get(cap) :
       print(" is present")
else:
         print("does is not present")
