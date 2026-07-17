class Textbook: #class
    def __init__(self,name,number): #Defining constructors
        self.N=name
        self.no=number

    def show(self):
        print("Name:",self.N,"\n","number:",self.no)




#Creating objects
t1=Textbook("Mritiyunjay",111)
t2=Textbook("Agnipankha",112)

#Calling function
t1.show()
t2.show()