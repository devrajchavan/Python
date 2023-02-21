# 1. Encapsulation = Encapsulation is used to restrict access to methods and variables.
#                    In encapsulation, code and data are wrapped together within a single unit.

# 2. Public Member = Accessible anywhere from otside oclass.
# 3. Private Member = Accessible within the class only '''(Syntax : double underscore __a)'''
# 4. Protected Member = Accessible within the class and its sub-classes only '''(Syntax : single underscore _a)'''




# Example 1 --------------------------------------------

'''class  Base:
    def __init__(self):
        print("Parent Class constructor called !")
        self._a = 2

class Derived(Base):
    def __init__(self) :

        Base.__init__(self) #--> Calling the base class constructor using SUPER keyword or uisng BASEclass name 

        print(self._a)  #--> Calling the protected member of base class

obj1 = Derived()
# print(obj1.a)    #--> calling protected member --> NOT POSSIBLE!!

obj2 = Base()
# print(obj2.a)    #--> calling protected member --> NOT POSSIBLE!!
'''



# Example 2 -------------------------------------

'''class Base:
    def __init__(self):
        print("Parent Class constructor called ")
        self.a = "YCCE"     # Public Member
        self.__c = "IIM"    # Private Member

class Derived(Base):
    def __init__(self):

        Base.__init__(self)  #--> Calling the base class constructor using SUPER keyword or uisng BASE class name
        print(self.__c)      #--> Calling the PRIVATE member of base class

obj1 = Derived()
print(obj1.a)
print(obj1.c)

obj2 = Base()
print(obj2.a)
print(obj2.c)
'''







