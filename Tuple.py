'''tuple1=(1,2,"college",9)
tuple2=() # creates an empty tuple
tuple3=tuple((1,3,5,9,"hello"))
print(tuple1)
print(tuple2)
print(tuple3)
#tuple1[2] = "Sunil"           # Not possible
print(tuple1)
#tuple1.append("Sunil")        # Not possible
print(tuple1)    '''


mytuple = ("Prashant", "Ashish", "Rahul", "Sandip", "Komal", "ankush", "Rajesh", 23,3,15,77,"sandip")
print(mytuple)
print(type(mytuple))
#mytuple[2] = "Sunil"   # Not Possible ...--> As tuple is immutable
print(mytuple)

mytuple = (mytuple + (14,22))
print(mytuple)


