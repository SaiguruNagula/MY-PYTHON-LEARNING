# file reading ( .txt , .json , .csv)


#txt
file_path = "C:/Users/hp/OneDrive/Desktop/output.txt"


try:
 with open(file_path , 'r') as file:
    content = file.read()
    print(content)
except FileExistsError:
  print("file not found ")
except PermissionError:
  print("u dont have the permission")

finally:
  print('FILE IS CLOSED')

# .json 
import json


file_path = "C:/Users/hp/OneDrive/Desktop/output.json"


try:
 with open(file_path , 'r') as file:
    content = json.load(file)                 # using .load method in json module 
    print(content) 
except FileExistsError:
  print("file not found ")
except PermissionError:
  print("u dont have the permission")

finally:
  print('FILE IS CLOSED')



# .csv
import csv


file_path = "C:/Users/hp/OneDrive/Desktop/output.csv"


try:
 with open(file_path , 'r') as file:
    content = csv.reader(file)                 # using .reader method in csv module 
    for line in content:                       # can be printed by iterating over each line (column)
     print(line) 
except FileExistsError:
  print("file not found ")
except PermissionError:
  print("u dont have the permission")

finally:
  print('FILE IS CLOSED')