# LOCAL VARIABLE = These variables are declared using SELF keyword
# INSTANCE VARAIBLE =  These are the varaibles whose values changes from object to object 
# STATIC VARIABLE = These are the variables whose value is constant/same for every object. STATIC VARIABLES are declared inside the CLASS , 
#                   but outside the FUNCTION !!



# EXAMPLE 1


'''class Student:
    def __init__(self):   #This is a Constructor which have a default parameter as self
        self.s_name = input("Enter your name")  
        self.s_rollno = 101   #Instance Variable aka Data Member
    def getdata(self):
        self.s_mb = 9090909090
obj = Student()     
obj.getdata()
obj.s_branch = "E&TC"  #Here we are declaring this value outside the class using the object
print(obj.s_name)
#del obj.s_rollno
print(obj.__dict__)
del obj.s_rollno
print(obj.__dict__)
'''



# Example 2


'''class Student:
    def __init__(self):
        self.s_name = "Devraj"
        self.l_name = "Chavan"
        self.s_rollno = 21
        self.s_branch = "E&TC"
        self.s_mb = 9090909090
obj = Student()

print(obj.__dict__)'''


# Example 3

'''class Hod:
    def __init__(self):
        self.name="DEVRAJ"
        self.age=20
        self.rollno=21

    def info(self):
        print("My Name is:", self.name)
        print("My Age is: ", self.age)
        print("My emp id:", self.rollno)

obj = Hod()

obj.info()'''



#Example 4

class College:
    
    collegename="DYPIT"                       #This is a static variable as it is outside the method and inside the class 

    def __init__(self):
        self.studentname= "Gaurav"            # Here studentname is a local vairable

principal = College()
teacher = College()
accountant = College()

principal.studentname="Pratik"
# teacher.studentname="Devraj"

print("Principal",principal.collegename,"...",principal.studentname)
print("Teacher", teacher.collegename,"...",teacher.studentname)
print("accountant", accountant.collegename,"...",accountant.studentname)

print("---------------------------------------------------")

College.collegename="DY AKURDI" #using the classname we can access the static VARIABLE
principal.studentname="Devraj CHavan"

print("principal =", principal.collegename,"|",principal.studentname)
print("teacher ",teacher.collegename,"|",teacher.studentname)
print("accountant",accountant.collegename,"|",accountant.studentname)
