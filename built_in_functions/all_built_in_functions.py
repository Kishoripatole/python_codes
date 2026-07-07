# 1)abs() function
a=-86.20
print("Absolute value of a:",abs(a))


# 2)all() functions behaves as AND rule(It returns true if all items/ 
# in the passed iterable are true.)
b=[1,2,3,8]
print(all(b))
c=(10,20,0,40)
print(all(c))

# 3)bin() function represents binary digits
x=68
print(bin(x))

# 4)bool() function (returns either true or false)
test1 = []  
print(test1,'is',bool(test1))  
test1 = [0]  
print(test1,'is',bool(test1))  
test1 = 0.0  
print(test1,'is',bool(test1))  
test1 = None  
print(test1,'is',bool(test1))  
test1 = True  
print(test1,'is',bool(test1))  
test1 = 'Easy string'  
print(test1,'is',bool(test1))  

# 5)bytes() function represents b symbol beffore printing string
string="Hello world"
b=bytes(string,'utf-8')
print(b)

#6)callable() function
def x():
    print(8)
print(callable(x))

#7) compile() function
code='x=12\ny=12\nprint("sum:",x+y)'
code_sum=compile(code,'sum.py','exec')
print(type(code_sum))
exec(code_sum)
