#
import pandas as pd

df=pd.read_csv("Pandas/people_100.csv")
print(df)

#to print first some lines
print(df.head(10))

#to print last some lines
print(df.tail(2))

