class Textbook:
    def __init__(self,name,writer):
        self.name=name
        self.writer=writer

class name_of_book(Textbook):
        def show(self):
         print("Name of the book:",self.name,"\n","Writer:",self.writer)


n1=name_of_book("Agnipankha","Dr.A.P.J.Abdul Kalam")
n2=name_of_book("Ek Hota Carver","Veena Gavankara")
n3=name_of_book("Mrityunjay","shivaji Sawant")


n1.show()
print("--------------------------")
n2.show()
print("-------------------------")
n3.show()