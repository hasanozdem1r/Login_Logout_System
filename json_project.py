import json,os
class User(object):
    #constructor(initializer)
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    #constructor(initializer)
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False #we accept user defaul logout
        self.currentUser={}
        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"): #this is check this file is available or not
            with open("users.json","r",encoding="utf-8") as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user) # convert from string to json 
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users) #print user object

    def register(self,user:User): #parameter name is user and user type is User
        self.users.append(user)
        self.saveToFile() #to add all list to file
        print("User created")
        print(repository.users)

    def login(self,username,password):
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedIn=True
                self.currentUser=user
                print("Login succesful")
                break
        else:
                print("Login unsuccesful")
    def logout(self):
        #logout
        self.isLoggedIn=False
        self.currentUser={}
        print("Logout succesful")
    def Identity(self):
        #Identity
        if self.isLoggedIn:
            print(f"username:{self.currentUser.username}")
        else:
            print("No Login")
    def saveToFile(self):
        #json.dump accept just builtin types
        listForJson=[]
        for element in self.users:
             listForJson.append(json.dumps(element.__dict__)) #__dict__ convert element object to dict
        with open("users.json","w") as file:
            json.dump(listForJson,file) #json.dump accept just builtin types

repository=UserRepository()

while True:
    print("Menu".center(26,"*"))
    secim=input("1 - Register \n| 2 - Login \n| 3 - Logout \n| 4 - Identity \n| 5 - Exit ")
    if secim=="5":
        break
    else:
        if secim=="1":
            #register
            username=input("Username:")
            password=input("Password:")
            email=input("Email:")
            user=User(username=username,password=password,email=email)
            repository.register(user)
        elif secim=="2":
            #Login
            if repository.isLoggedIn:
                print("Already logged in")
            else:
                username=input("Username:")
                password=input("Password:")
                repository.login(username,password)
        elif secim=="3":
            #Logout
            repository.logout()

        elif secim=="4":
            #Identity display username
            repository.Identity()
            
        else:
            #unexpected input 
            print("Wrong option please choose again")
            
