# List: Different data types in square brackets
a=[10,20,40.25,"tulip",74,1/4,2-1,3+4,5*8,"Dahlia",5+6j]
print(a)

#accessing elements from the list
print(a[1])
print(a[3:])
print(a[-1])
print(a[1:10])
print(a[::-1])


#updating elements of the list
a[8]="a+ib"
print(a)


#adding elments to the list
a.append("daisy") #adding single element to the end of list
print(a)
a.insert(1,"Allium cepa")# add element at the specific index
print(a)

a.extend([86.20,71])# adding multiple elements to the end of list
print(a)

#removing elements from the list

a.remove(20) #removing first occurrence
print(a)

a.pop(-3) #"removing by index or last element by default"
print(a)

del a[0] #deleting element
print(a)


#iteration by loop

b="Mangifera Indica"
for i in b:
     print(b)
     

N=[1,2,3,4,5,6,7,8,9,10]
n=0
while n<len(N):
     print(N[n])
     n+=1


#Sorting a list
a_1=[12,20.45,85,36,35,74]     
print("list created:",a_1)

a_1.sort()
print("sorted list:",a_1)

#reversing list
a_1.reverse()
print("Reverse list:",a_1)

#Finding largest and smallest number in list
b=[71,86.20,61,62,49,68,58]
print("Printed list:",b)
print("Largest of the list:",max(b))
print("Smallest of the list:",min(b))

#Calculating sum of the list
c=[71,86.20,61,62,49,68,58]
print("Sum of the list:",sum(c))

d=[71,86.20,61,62,49,68,58]
print("length of the list:",len(d))

print("Clearing list:",d.clear())