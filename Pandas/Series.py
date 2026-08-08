print("----printing series----")
import pandas as pd
a=[1,2,3,4,5]
one=pd.Series(a)
print(one)
print("\n")

#To access specified value
print("print 2nd index")
d=["monday","saturday","sunday"]
e=pd.Series(d)
print(d[2])
print("\n")


#create lables
print("print with index")
b=[10,20,30,40]
two=pd.Series(b,index=["0","1","2","3"])
print(two)
print("\n")

#Key/Value Objects as Series
print("----dictionary----")
c={"monday":1,"tuesday":2,"wednesday":3,"thursday":4}
d=pd.Series(c)
print(d)
print("\n")

e=pd.Series(c,index=["monday","tuesday"])
print(e)