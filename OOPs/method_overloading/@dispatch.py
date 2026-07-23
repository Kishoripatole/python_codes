 
from multipledispatch import dispatch 

class Simple_Calculator:  
  
  
  @dispatch(int, int)  
  def add(self, a, b):  
    return a + b  
  
   
  @dispatch(float, float)  
  def add(self, a, b):  
    return a + b  
  
   
  @dispatch(int, float)  
  def add(self, a, b):  
    return a + b  
  
    
  @dispatch(float, int)  
  def add(self, a, b):  
    return a + b 
my_calculator = Simple_Calculator()  
 
print(my_calculator.add(9, 14)) # int + int  
print(my_calculator.add(3.72, 1.54))  # float + float  
print(my_calculator.add(12, 5.2))  # int + float  
print(my_calculator.add(1.7, 0.56))  # float + int  