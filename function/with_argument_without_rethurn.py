
def fun(x):
    print("add:",x)

fun(7)



x = 10  # global variable    
def my_function():    
    y = 5  # local variable    
    print("Inside function:", "x =", x, ", y =", y)    
  
my_function()    
  
print("Outside function:", "x =", x)   