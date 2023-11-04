class rps:
    ap=0
    bp=0
    
    def enter(self):
        self.aa=input("enter your name(player 1):")
        self.bb=input("enter your name(player 2):")
        self.start()


    def start(self):
        print ("welcome to game rock paper scissors!")
        print("enter 1 for rock")
        print("enter 2 for paper")
        print("enter 3 for scissor")

        a=input(f"{self.aa} enter your option:")
        b=input(f"{self.bb} enter your option:")

        if a==b:
            print("draw")
            self.paa()
        elif a=="1" and b=="2" or a=="2" and b=="3" or  a=="3" and b=="1":
            print(f"{self.bb} is winner!!")
            self.bp+=1
            print(f"{self.bb} score is {self.bp}")
            self.paa()
        else:
            print(f"{self.aa} is winner!!")
            self.ap+=1
            print(f"{self.aa} score is {self.ap}")
            self.paa()


    def  paa(self):

        p=input("want to play again: yes or no:")
        if p=="yes":
            self.start()
        else:
            self.dec()

    def dec(self):
        if self.ap>self.bp:
            print(f"{self.aa} scored {self.ap} points and won!!")
        elif self.bp>self.ap:
            print (f"{self.bb} scored {self.bp}points and won!!")
        else:
            print("match drawn!!")

x=rps()
x.enter()
