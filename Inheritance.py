'''class Faculty:
    def __init__(self, name, dept, id):
        self.name = name
        self.dept = dept
        self.id = id

    def print_info(self):
        print("Faculty information : ", self.name, self.dept, self.id)

# obj = Faculty("Ashish", "CS", 101)
#obj.print_info()
#===========================================================
class CSE(Faculty):
    pass

obj = CSE("Jyoti mam", "Computer Sci", 102)
obj.print_info()
#===========================================================
class Me(Faculty):
    pass

obj = Me("XYZ mam", "Science", 103)
obj.print_info()
'''



#-----------------SINGLE LEVEL INHERITANCE----------------------------
'''class College :
    def college_name(self):
        print("D Y PATIL")

class Student(College):
    def student_info(self):
        print("Name : Devraj CHavan")
        print("Branch : E&TC")

obj = Student()
obj.college_name()

obj.student_info()
'''

#------------------MULTILEVEL INHERITANCE-----------------------------
'''class College :
    def college_name(self):
        print("D Y PATIL")

class Student(College):
    def student_info(self):
        print("Name : Devraj CHavan")
        print("Branch : E&TC")

class Exam(Student):
    def subject(Self):
        print("Subject 1 : PDC")
        print("Subject 2: PM")
        print("Subject 3: CN")
        print("Subject 4: Advance Java")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()
'''


#-------------------------MULTIPLE INHERITANCE------------------------
'''class SubMarks:
    math = int(input("Enter Mathematics marks : "))
    sci = int(input("Enter Science marks : "))

class PractMarks:
    sci_pract = int(input("Enter Science Practical marks : "))

class Result(SubMarks, PractMarks):   #--> CHild Class

    def total(self):
        if self.math>=40 and self.sci>=40 and self.sci_pract>=20:
            print("You are Pass !")
        else :
            print("You are Failed !!")

obj = Result()
obj.total()
'''









