class Textbook:
    def __init__(self,name,number):
        self.N=name
        self.no=number

    def show(self):
        print("Name:",self.N,"\n","number:",self.no)



t1=Textbook("Rehana",1356)
t2=Textbook("Aishwarya",5)

t1.show()