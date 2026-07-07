
for a in range(1,100):
    print(a)
    a=a+1


for n in range(2,10):
    print("10 x ",n,"=",n*10)
    n=n+1

flowers=["Tulip","jasmine","Tulip","Dahlia","Daisy","Gulchadi",
         "Chapha","mogra","lily","Parijatak","lotus","Orchid",
         "sunflower","bluelily","merrygold","Ratrani","Lajalu","Lavender","Vanilla"]
for types in flowers:
    print(types)

print("Odd numbers:")
for i in range(1,11,2):
    print(i,end="--")
    continue

print("Numbers:")
for i in range(1,10,2):
    print(i)
    


print("Even numbers:")
for i in range(1,100):
    if i%2==0:
      print(i)
    continue

print("print even numbers:")
for i in range(1,10,2):
    print(i,end="")

