# file writing files (.txt , .json , .csv)

#.txt

#txt_data= "i like pizza!"

#file_path = "C:\\Users\\hp\\OneDrive\\Desktop\\output.txt"

#with open(file_path , 'w') as file :
 #   file.write(txt_data)
  #  print(f"txt file was created :{file_path}")



# .json
# import json
#js_data = {"name": "saiguru",
        #   "age" :18 ,
         #  "year":2025,
         #   "job":"AiML engineer"}


#file_path = "C:\\Users\\hp\\OneDrive\\Desktop\\output.json"

#try:
 #with open(file_path , 'w') as file :
  #  json.dump(js_data, file, indent= 4)                                     # json.dump(data , file )
   # print(f"json file was created :{file_path}")

#except Exception:
 #  print("invalid error")


# csv (comma seperated values)
import csv

cs_v_data = [["name" , "age" , "job"],
             ["spongbob", 20,"cook"],
             ["squidward",30,"manager"],
             ["patrick",27, "cashier"]]

file_path = "C:\\Users\\hp\\OneDrive\\Desktop\\output.csv"     # .csv

try:
  with open(file_path, 'w') as file :
    write = csv.writer(file)          # to write , create a writer object and acceess from csv writer() method
    for row in cs_v_data:
      write.writerow(row)
    print(f"csv file was created :{file_path}")
except FileExistsError:
  print("file existance error")
