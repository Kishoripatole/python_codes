from functools import singledispatchmethod

class calculator:

    @singledispatchmethod
    def add(self,a,b):
        raise NotImplementedError("Unsupported Data type")
    @add.register
    def _(self,a:int,b:int)-> int:
        return a+b
    @add.register
    def _(self,a:float,b:float)->float:
        return a+b


cal=calculator()

print(cal.add(2,4))
print(cal.add(2.2,4.5))
try:
    print(cal.add("tulip","dahlia"))
except NotImplemented as e:
    print(e) 