from abc import ABC

class Bird(ABC):

    def sound(self):
        pass
    
    
class Peacock(Bird):
    def sound(self):
        print("Cavvvvvv.............!")


p=Peacock()
p.sound()