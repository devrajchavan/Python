#1. Module is imported using a import keyword 
#2. Module contains functions, classes, and variables that we can use in another program

#First way -->

import module1
module1.cube(4)
module1.login("Devraj", "Devraj")
print(module1.pi)
module1.welcome1()
module1.welcome("Devraj", "Chavan")

#Second way -->
'''import module1 as mod
mod.cube(4)
mod.login("Devraj", "Devraj")
print(mod.pi) 
mod.welcome()
mod.welcome("Devraj", "Chavan")    '''

#Third way -->
'''from module1 import pi, cube, welcome, login
cube(4)
login("Devraj", "Devraj")
print(pi)
welcome()
welcome("Devraj", "Chavan") '''

#Fourth way

'''from module1 import*
cube(4)
login("Devraj", "Devraj")
print(pi)
welcome()
welcome("Devraj", "Chavan")'''


