# creating a class  
class Simple_Calculator:  
  # defining a function to add numbers  
  def add(self, a, b = 0, c = 0,d=0):  
    '''
    This method has few default parameter values set to 0 
    ''' 
    return a + b + c +d 
  
# creating an object  
C = Simple_Calculator()  
  
# calling the add() method  
print(C.add(3)) # single argument  
print(C.add(3, 6)) # two arguments  
print(C.add(3,6,9)) # three arguments 
print(C.add(3,6,9,12))  