#lambda function with multiple arguments
a=lambda b,c:b%c
b=int(input("Enter b:"))
c=int(input("Enter c:"))
print(a(b,c))


x=lambda p,q:p/q
print(x(169,13))


b=lambda x,y,z:x*y*z
print(b(1,24,2))



c=lambda a,b,c:a+b+c
print(c(1,1,2))