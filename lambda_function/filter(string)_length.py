a=["apple","banana","custrad apple","mango","chikoo"]
b=["gulchadi","parijatak","sunflower","Daisy","merigold"]


fruits1=filter(lambda a:len(a)>6,a)
fruits2=filter(lambda a:len(a)==6,a)
fruits3=filter(lambda a:len(a)<7,a)

print(list(fruits1))
print(list(fruits2))
print(list(fruits3))

