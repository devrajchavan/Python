'''list1=[1,4,"Gitam",6,"college"]
list2=[]  # creates an empty list
list3=list((1,2,3))
print(list1)
print(list2)
print(list3)
print(list1[4])
list1.append(34)
print(type(list1))
print(list1[::-1])
list1[2] = "Harsh"
print(list1)
list1.insert(3,"Sanket")
print(list1)
list1.remove("college")
print(list1)                '''

mylist = ["Prashant", "Ashish", "Komal", "Ankush", 77, "Sandip", "Prashant", 3.142]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[: : -1])
print(mylist[1:8:2])

mylist[2] = "Rushad"
print(mylist)

mylist.append("Sunil")
print(mylist)

if "ankush" in mylist:
    print("Yes, ankush is present")
else:
    print("Not available")

mylist.insert(3, "Devraj")
print(mylist)

