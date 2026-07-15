class Car:    
    def __init__(self, name, color):    
        self.name = name    
        self.color = color    
  
    def show_details(self):    
        print("Car Name:", self.name)    
        print("Color:", self.color)    
  
# creating objects    
car1 = Car("Honda City", "White")    
car2 = Car("Hyundai Creta", "Black")    
  
# calling method    
car1.show_details()    
print()    
car2.show_details()    
     
    