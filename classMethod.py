# class method = Allows operation related to class itself 
#                take (cls) as a first parameter 

# instance method = best for opertation used on the instance of the class (instance)
# Static methid = best for utility function that do not need acces to the class data
# class method = best for class level data or require access to class itself


class student:
    count= 0
    totalgpa = 0

    def __init__(self, name , gpa):
        self.name = name
        self.gpa =gpa
        student.count += 1
        student.totalgpa += gpa

    def get_info(self):
        print(f"name : {self.name} and gpa : {self.gpa}")

    @classmethod
    def avg_cgpa(cls): 
        avg=0
        if cls.count==0:
           return 0
        else :
           return  cls.totalgpa/cls.count
        

stu1 = student("saiguru", 9)
stu2 = student("labdhi ", 10)
stu3= student("pandit",9)

stu1.get_info()
stu2.get_info()
stu3.get_info()
print(student.avg_cgpa())




    