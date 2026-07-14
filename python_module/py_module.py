import calculator as  cal 


print(cal.add(10,20,30,40,50,60,70,80))
print(cal.sub(4,4))
print(cal.multiplication(20,40))
print("Division:",cal.division(180,45))
print(cal.remainder(40,10))
print("Q:",cal.quotient(50,40))

from  calculator import remainder as r
from calculator import quotient as q
from calculator import division as d
print(r(60,7))
print(q(12,6))
print(d(78,1))