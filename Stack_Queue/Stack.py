'''
import time
myStack = []     #--> empty stack 

size = int(input("Enter size of stack : "))

for i in range(size):
    a = int(input("Push Element in Stack : "))
    myStack.append(a)
else:
    print("Stack is Full !!")
    print(myStack)

print("Pop operation started : ")
for i in range(size):
    time.sleep(3)
    print(myStack.pop(), "pop element from the stack !")
else:
    print("Stack is Empty !")
    print(myStack)
'''

# ---------------------------------------------------------------
# Example 2

'''stack = []
for top in range(5):
    a = int(input("Push a element in stack "))
    stack.append(a)
    top +=1
else:
    print("Stack is Full !")

print("STack = ", stack)
print("Top =", top)

#==============

for i in range(5):
    print(stack.pop())
    top -= 1
else:
    print("Stack is Empty")

print("STack = ", stack)
print("Top =", top)
'''
# Checking whether Stack is empty, full or fre space using TOP value !
def stack(myList):
    for top in range(len(myList)):

        if top>0:
            print("Stack is Full !!")
            break
    else:
        print("Stack is Empty !")

myList = []
stack(myList)
















