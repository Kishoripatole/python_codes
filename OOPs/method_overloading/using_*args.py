class calculator:
    def add(self,*args):
        return sum(args)


cal=calculator()

print(cal.calculator(1))
print(cal.calculator(1,3))
print(cal.calculator(1,3,5))