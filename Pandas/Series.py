
import pandas as pd
a=[1,2,3,4,5]
one=pd.Series(a)
print(one)

#To access specified value
d=["monday","saturday","sunday"]
e=pd.Series(d)
print(d[2])


#create lables
b=[10,20,30,40]
two=pd.Series(b,index=["0","1","2","3"])
print(two)

#Key/Value Objects as Series
c={"monday":1,"tuesday":2,"wednesday":3,"thursday":4}
d=pd.Series(c)
print(d)