'''
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
try:
    print(a/b)
except:
    print("Division by zero condition !!, Please enter valid divisor ") '''

'''
try:
    print(2/0)

except ZeroDivisionError as message:            #division by zero
    print("The description of exception : ", message)   '''

# Multiple except block
try:
    a = int(input("Enter 1st integer number : "))
    b = int(input("Enter 2nd integer number : "))

    print(a/b)
except ZeroDivisionError as message:
    print("Division by zero not possible : ", message)
except ValueError as message:
    print("Enter only integer number=", message )

#Handling multiple different kinds of exception with single except block
try:
    a = int(input("Enter 1st integer number : "))
    b = int(input("Enter 2nd integer number : "))
    print(a/b)
except(ValueError, ZeroDivisionError) as message:
    print("Enter correct number : ", message)
except:
    print("This is default part of except block")

#Finally Block is always executed 
try:
    a = int(input("Enter 1st integer number : "))
    b = int(input("Enter 2nd integer number : "))
    print(a/b)
except(ValueError, ZeroDivisionError) as message:
    print("Enter correct number : ", message)
finally:
    print("I will always executed")

# Nested try except block
try:
    a = int(input("Enter 1st integer number : "))
    b = int(input("Enter 2nd integer number : "))
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print(msg)
except ValueError as msg :
    print(msg)
    


