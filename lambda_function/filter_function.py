y=[10,20,3,40,50,60]

is_even=filter(lambda a: a%2==0,y)
is_odd=filter(lambda b: b%2!=0,y)

print(list(is_even))
print(list(is_odd))
