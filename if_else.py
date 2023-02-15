#Write a python code to find largest number from the 3 numbers
'''a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

largest = 0

if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c

print(largest, "is the largest of three numbers.")'''



#Write a python code to find positive, negative and zero number
'''
num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num < 0:
   print("It is a negative number")
else:
   print("It is a zero")   '''



#Write a python code to find eligibilty for Driving License
''' age = int(input("Enter your age : "))

if age > 18 :
    print("You are Eligible")

else:
    print("You are not eligible")  '''



#Write a python code to check whether student is passed or failed in every subject (passing num = 40 Marks)
'''a = int(input("Enter marks for subject 1 : "))
b = int(input("Enter marks for subject 2 : "))
c = int(input("Enter marks for subject 3 : "))
d = int(input("Enter marks for subject 4 : "))

percentage = ((a+b+c+d)/400) * 100

if a>=40 and b>=40 and c>=40 and d>=40 :
    print(f"You are Pass, you got {percentage} percentage!!")
else :
    print(f"You are Fail, you got {percentage} percentage!!")  '''


#Write a python code whether a alphabet is vowel or consonant
'''letter = input("Enter a character : ")

vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if letter in vowel_list :
    print(f" '{letter}' is a vowel")

else :
    print(f" '{letter}' is a consonant")  '''


#        ASCII Value
#     65-91  --> A - Z  (uppercase)
#     97-122 --> a- 7   (lowercase)
#     48-57  --> Numbers(0 to 0)
#     ord() --> method is used to convert character to ASCII values

#Write a python code to find total number of vowels present in given name using if-else



# Write a python code to to find character is in uppercase or in lowercase
'''ch = ord(input("Enter any charater : "))
if ch>=65 and ch<=91:
    print("entered charachter is uppercase")
elif ch>=97 and ch<=122:
    print("entered character is in lowercase")
elif ch>=48 and ch<=57 : 
    print("entered character is digit")
else :
    print("entered character is special symbol")   '''


#Write a simple python code of if_else
'''brand = input("Enter your Cold-Drink brand : ")

if brand == "pepsi" or brand == "PEPSI":
    print("Swag...")
elif brand == "deo" or brand == "Deo":
    print("dar ke aage jeet hai...")
elif brand == "thumsup" or brand == "THUMSUP":
    print("taste the thunder...")
else : 
    print("GO with your brand...")      '''


#Write a code to find the sum of first 'n' natural numbers using if-else not using loops

''' n = int(input("Enter a number : "))
sum = 0

while n > 0:
    sum = sum + n
    n = n-1

print(sum)    '''


#Write a code for Fibonacci Series 
'''n = int(input("Enter a number :"))
a = 0
b = 1
count = 0

while count < n :
    print(a)
    c = a+b
    a=b
    b=c
    
    count = count + 1 '''







