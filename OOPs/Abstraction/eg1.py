
from abc import ABC, abstractmethod    
  
# abstract base class    
class Vehicle(ABC):    
 
    @abstractmethod    
    def start(self):    
        pass    
 
    @abstractmethod    
    def stop(self):    
        pass    
  
# child class    
class Car(Vehicle):    
  
    def start(self):    
        print("Car is starting with a key ignition.")    
  
    def stop(self):    
        print("Car is stopping using the brake.")    
  
# creating object of child class    
my_car = Car()    
my_car.start()    
my_car.stop()
