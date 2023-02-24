class Nodes:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =  None

# Creating a object of Linked Lit and assigning a NULL value 
linked_list = LinkedList()
linked_list.head = Nodes(1)
second = Nodes(2)
third = Nodes(3)

#Connect the Nodes
linked_list.head =second
second.next = third 

#print the linked list items 
while linked_list.head != None:
    print(linked_list.head.data, end=" ")
    linked_list.head = linked_list.head.next







# Road Map for Next 5 Months !
# Aptitude

# March --> HackerRank -- Python -- 
#           Daily 5 questions (2 Hours minimum)

# April, May, June  --> Data Structures and Algorithms (2.5 Month)
            #           1. Hacker Rank
            #           2. DSA Sheet --> Apna College
            #           3. DSA Sheet --> Love Babbar
            #           4. DSA Sheet --> Striver (Refer only After Finishing DSA)

# July --> OOPS, OS, DBMS

# Also Make Digital/HandWritten Notes                                                                                           





       
