#validate user input exercises
# username is no more than 12 character
# user name mut not contain spaces 
#user name must not contain digits

Username= input("enter user name : ")

len= len(Username)

if len> 12 :
    print("username should be less than 12 char")
    
     
elif Username.isalnum():
    print("username should not contain digits")
   
elif  Username.find(" ")>= 0:
    print("username should not contain spaces")
    
else:
    print("username is valid")