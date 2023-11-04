class contacts:
    contacts=dict()

    def opera(self):
        while(True):
            print("enter 1 for adding contact")
            print("enter 2 for deleting contact")
            print(" enter 3 for seeing all contacts")
            print(" enter 4 for update contact")
            print(" enter 5 for search contact")

            a=input("enter your operation:")
            if a=="1":
                self.add()
            elif a=="2":
                self.dele()
            elif a=="3":
                self.list()
            elif a=="4":
                self.update()
            elif a=="5":
                self.search()


    def add(self):
        self.name=input("enter name :")
        self.num=int(input("enter the phone number:"))
        self.mail=input("enter mail of contact:")
        self.adress=input("enter the address of contact: ")
        self.contacts[self.name]=[self.num,self.mail,self.adress]
        print(f"successfully added {self.name} to contact")

    def dele(self):
        b=input("enter the name of contact to delete:")
        if b in self.contacts:
            self.contacts.pop(b)
            print(f"deleted the contact {b}") 
        else:
            print("contact not found")

    def list(self):
        for i in self.contacts:
            print("->",i , self.contacts[i])

    def update(self):
        b=input("enter the name of contact to update:")
        if b in self.contacts:
            c=int(input("enter the number of contact"))
        else:
            print("no contact found with")
        self.contacts[b]=c

    def search(self):
        d=input("enter a name to search:")
        if d in self.contacts:
            print(f" the details of the contact is {self.contacts.get(d)}")
        else:
            print("contact not found!!")


a=contacts()
a.opera()
        
