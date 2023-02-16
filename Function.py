'''def login() :            # --> Declaring the function
    while True:
        username = input("Enter username : ")
        password = input("Enter Password : ")

        if username == password :
            print("Login Succesfull !!")
            break
        else : 
            print("Login Failed !!")

print("Login page ")
login()        # --> Calling the function  '''

'''
import time
def msg() :
    print ("Hello, World !!")

msg()
time.sleep(3)
msg()
time.sleep(2)
msg()  '''

'''
def info(firstname, lastname) :
    print("First Name  = " , firstname)
    print("Last Name = ", lastname)

info("Devraj", "Chavan")
info(lastname="Devraj", firstname="Chavan") '''


'''
def square(value):
    print("The square of two numbers is = ", value * value)

num = int(input("Enter a number : "))
square(num)  '''

'''
def arithmetic(a,b) :
    r = a + b
    n = a * b
    m = a - b

    return r,n,m

a = int(input("Enter 1st Number : ")) 
b = int(input("Enter 2nd Number : "))

print("Result :",arithmetic(a,b))       '''


'''def chk_even_odd(number) :
    if number%2 == 0:
        print(f"{number} is even number !!")
    else :
        print(f"{number} is NOT even number !!")

number = int(input("Enter a number : "))
chk_even_odd(number) ''' # --> calling function




#---------Day 4 (Session 2)--------------

#defualt argument
'''def func(city = "Nothing") :
    print("I love", city)

func("Pune")
func("Delhi")
func() '''


#Returning Multiple values
'''
def add_product(a, b):
    add = a + b
    product = a * b
    return add, product

num1 = int(input("Enter 1st Value : "))
num2 = int(input("Enter 2nd Value : "))
x, y = add_product(num1, num2)

print("Addition is = ", x)
print("Product is = ", y)               '''


#Traversing a String
'''
def func(name):
    for i in name :
        print(i)

n = input("Enter a string : ")
func(n)                         '''


#Traversing a list
'''
def func(name):
    for i in name :
        print(i)

n = ["Devraj", "Gaurav", "Kiran", "Pratik", "Atharva"]
func(n)                     '''


#Returning the index of specified character in the given string 
'''
def func(name):
    j = 0
    for i in name :
        if i == 'v':
            print("The character 'v' is present at index number",j,"in a given name ",name )
            break
        j=j+1

name = input("Enter your name :")
func(name)   '''









