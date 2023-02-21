'''
1. ABSTRACT CLASS = A class which contains one or more abstract methods 
                    is called abstract class. 

2. ABSTRACT METHOD = A method which that has a declaration but does not have implemenatation

3. ABSTRACT class is considered as an BluePrint for other classes
4. It allows you to create set of methods that must be created within any child classes built from abstarct classes

'''


# Example 1 ------------------------------------------------

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides ")

class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides ")

class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides ")

class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides ")


t = Triangle()
t.noofsides()

p = Pentagon()
p.noofsides()

h = Hexagon()
h.noofsides()

q = Quadrilateral()
q.noofsides()



#Example 2 ---------------------------------------------------------
from abc import ABC, abstractmethod

class Programming(ABC):
    @abstractmethod
    def training(self):
        pass

    @abstractmethod
    def placement(Self):
        pass

class Devraj(Programming):
    def training(self):
        print("C, C++, Java")
    def placement(self):
        print("Java Placemnt !!")

class Farzin(Programming):
    def training(self):
        print("Python, Django")
    def placement(self):
        print("Python Placement !!")

class Gaurav(Programming):
    def training(self):
        print("machine learning")
    def placement(self):
        print(" Data science Placement!!")


obj1 = Devraj()
obj1.training()
obj1.placement()


obj2 = Farzin()
obj2.training()
obj2.placement()


obj3 = Gaurav()
obj3.training()
obj3.placement()



