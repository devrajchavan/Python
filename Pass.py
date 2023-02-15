#Example of Pass
myList = [1, 2, 3, 4, 5]
for n in myList:
    if n == 3:
        pass
    print(n)
print('--------------------------------')

#Example of continue
myList = [1, 2, 3, 4, 5]
for n in myList:
    if n == 3:
        continue
    print(n)
print('--------------------------------')

#Example of break
myList = [1, 2, 3, 4, 5]
for n in myList:
    if n == 3:
        break
    print(n)