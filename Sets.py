myset = {1, 2, "Sanjay", 5.66, "Rahul", "Ayush", "Ramesh", "Ankit", "Rishikesh"}

print(myset)
myset.add(60)
print(myset)

'''myset.discard(3)
print(myset)
myset.remove(3)
print(myset)'''

#pop() --> Method used to remove the object from last !!

#union() --> This method will return newset
myset = {10,20,30,40}
yourset = {40,50,60,30}
newset = myset.union(yourset)
print(newset)

#intersection() --> This method will return common element
myset = {10,20,30,40}
yourset = {40,50,60,30}
newset = myset.intersection(yourset)
print(newset)

#difference() --> This method will return the element in myset but not in yourset
myset = {10,20,30,40}
yourset = {40,50,60,30}
newset = myset.difference(yourset)
print(newset)

#clear() --> Method used to clear data