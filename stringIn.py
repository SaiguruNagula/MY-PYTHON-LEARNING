name= "Saiguru"
friend = "labdhi"
anotherFriend = 'Pandit'
apple ="hi , i want to eat an apple"
apple2="he said , 'i want an apple'"  #  output = he said , 'i want an apple'

print(apple)
print(apple2)

# multiline string
# triple single quote ''' ......  '''
mango ='''he said that ,
i want 5 kg mangoes to make mango ice cream 
plus some fresh milk '''
print(mango)

# in python string is like array of character 
print(name[0]) # S
print(name[1]) # a
print(name[2]) # i


#slicing in python
name2= "labdhi"

#we can find length of string using len() fn

print(len(name2)) # output 6

print(name2[0:4])  # 4th index is excluded  output labd

print(name2[:4])  # auto start from 0

print(name2[0:-3])  # negative indexing also equals to len-3= 3 = lab

print(name2[-1]) # to get last index = i

#quiz ans
nm='harry'
print(nm[-4:-2])  #ans ar


# String Methods
# ( STRINGS are immutable)  it creats new string 
a= 'ha arry !!'

print(len(a)) # len() gives length of fm

print(a.upper()) # .upper()  converts sting to upper case
print(a.lower())  # .lower() cinverts to lower case
print(a.rstrip("!")) # remove any character from string
print(a.replace("haarry","star")) # replace all the occurance of given string

print(a.split( " ")) #The split() method splits the given string at the specified instance and returns the separated strings as list items

blog= "introduction to js"
print(blog.capitalize()) #The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
                         # The string has no effect if the first character is already uppercase.
str1 = "Welcome to the Console!!!"
print(str1.center(100)) #The center() method aligns the string to the center as per the parameters given by the user.