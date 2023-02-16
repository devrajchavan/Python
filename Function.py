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



def validate(username, password) :
    
 print("1. Login")
print("2. Register")
choice = int(input("Enter your choice :"))
 
if choice == 1 :
     username = input("Enter Your UserName : ")
     password = input("Enter Your Pasword : ")

     validate(username, password)

     if (validate) :
        print("Login Successfull")
     else :
        print("Login failed !!")

else :
    id = input("Set username :")
    auth = input("Set password :")
    print("Account is created")







