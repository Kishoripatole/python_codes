from abc import ABC 

class flowers(ABC):
    def show(self):
        pass
    
class Tulip(flowers):
    def show(self):
         print("Tulip has very subtle,clean and airy fragrance!")


t=Tulip()
t.show()