#TypeCasting Example

# int() --> Used to convert in integer 

print(int(3.14))         #float    --> int
#print(int(10 + 5j))     #complex --> int                     Not Possible 
print(int(True))         #boolean -->  int
print(int(False))        #boolean -->  int
#print(int("4.22"))      #String -- > Float -- > int           Not Possible 
print(int("4"))          #String(number)--> int
#print(int("Devraj"))    #String(Characters)--> int            Not Possible 


# float()  --> Used to convert in float

print(float(3))
#print(float(10 + 5j))          Not Possible
print(float(True))
print(float(False))
print(float("4.22"))
print(float("4"))
#print(float("Devraj"))         Not Possible


# bool()  --> Used to convert in boolean

print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool(""))
print(bool("Devraj"))

#complex() --> Used to convert incomplex datatype 

print(complex(2))
print(complex(1.5))
print(complex(True))
print(complex(False))
print(complex("5.6"))
print(complex(5, -3))
print(complex(True, False))
print(complex(False, True))










