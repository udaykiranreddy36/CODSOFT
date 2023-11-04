class task:
    tasks=[]

    def choice(self):

        while(True):
            
            print("enter 1 for adding task")
            print("enter 2 for deleting task ")
            print("enter 3 for the tasks")

            a=input("enter your operation:")
          
            if a=="1":
                self.adding()
            elif a=="2":
                self.deleting()
            elif a=="3":
                self.task()
            else:
                print("no such operation")

    def adding(self):
        b=input("enter the task:")
        self.tasks.append(b)
        print(f"task {b} has been added successfully")

    def deleting(self):
        if len(self.tasks)>0:
            print(f" the taks to be completed are:{self.tasks}")
            task=input("enter task you want to delete:")
            if task in self.tasks:
                self.tasks.remove(task)
                print(f"removed {task} successfully!!")
        else:
            print("no more tasks to complete")
            print("add tasks to complete")

    def task(self):
        print(self.tasks)

a=task()
a.choice()



















