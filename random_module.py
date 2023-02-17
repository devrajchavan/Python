# random module --> This module defines several functions to generate random numebrs. 

from random import *
for i in range(5):       # 0 to 4
    print(random())

#To generate random integer between two fiven numbers(inclusive)
from random import *
for i in range(10):     #0 to 9
    print(randint(1, 100000))


#random float values between 2 given numbers 
from random import *
for i in range(10):
    print(uniform(1,10))


#Choice() function
#It does not return random number, But it will return a random object from the given list and tuple 

from random import *
List = ["red shirt", "blue shirt", "pink shirt", "brown shirt"]
for i in range(10):
    print(choice(List))

#For every python program, a special variable __name__ will be added internally.
#This variable store information regarding whether the program is executed as an individual program or as amodule
#If the program executed as an individual program then the value of this variable is 

def call():
    if __name__ == 'main':
        print("This is executable as a individual program")
    else :
        print("This is executed as a module from some other program")

call()