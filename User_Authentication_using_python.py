def login():
    username = input("Enter username :")
    password = input("Enter Password :")

    if username in database and password in database :
        print("Login Succesfull!!")
    else :
        print("Login failed !!")



database = ["Devraj", "1234"]
print("1: Login")
print("2: Register")
choice=int(input("Enter choice :"))

if choice == 1:
    login()

elif choice == 2 :
    user = input("Create username : ")
    database.append(user)
    word = input("Create pasword : ")
    database.append(word)
    print("Acount created succesfully !!")
    print("---------------------------------------")

    login()

else :
    print("Please, enter valid choice !!")
