# Linear Searching

def linear(lis, n, target):

    for i in range(n):
        if(lis[i] == target):
            print(f"Element is found at {i}")

        else:
            print("Element NOT found")

n = int(input("Enter size of List : "))
lis= []
for i in range(n):
    element = int(input(f"Enter the {i} element"))
    lis.append(element)

target = int(input("Enter element to find : "))


print(lis)

linear(lis, n, target)


