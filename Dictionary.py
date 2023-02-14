# 1. A dictionary can have duplicate VALUES, but it has only UNIQUE keys
# 2. A dictionary is absed on the Key - value pair. 


mydict = {
    "name" : "Devraj",
    "Profession" : "Developer",
    "empID" : 1001
}

print(mydict)
print(type(mydict))

mydict = {
101 : "prashant",
102 : "Ashish",
"103" : "Mohini",
"104" : "Triveni",
101 : "Ashish",
104 : "Ashish"
}
 
print(mydict)

a = mydict[102]
print(a)













