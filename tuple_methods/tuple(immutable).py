a=("\"Dahlia\"",12.89,12,[12,"daisy",86.20],12*7,12+45j)
print(a)
print(type(a))

#accessing elements in tuple
b=("Tulip",12.25,20,[12,13,14,15,16,17])
print("Element_[0]:",b[0])
print("Element_[0]:",a[0])
print("Elment_[1]:",a[3])
print("Element_[-1]:",a[-1])
print("Element_[-2]:",a[-2])
print("Element_[-1]:",b[-1])
print("Element_[3][0]:",b[3][0]) #accessing element of list in tuple
print("Element_[-1][-1]:",b[-1][-1])

#slicing elements in tuple
c=(12,14,16,18,20,22,24,26,28,"Dahlia",[10,20,30,40])
print("element_[:5]:",c[:5])
print("element_[4:]",c[4:])
print("element_[0:11]:",c[0:11])
#accessing letters of string in tuple
print("element_[9][0]:",c[9][0])
print("element_c[9][1]:",c[9][1])
print("element_c[9][2]:",c[9][2])
print("element_c[9][3]:",c[9][3])
print("element_c[9][4]:",c[9][4])
print("element_c[9][5]:",c[9][5])

#Deleting tuple
d=("\"Tulip\"",12,14,24,86.20,49,"cherryblossom","Switzerland")
print("Printing tuple first:",d)
del d

#Changing elements in tuple
scientific_names=("allium cepa","mangifera indica","triticum Astivum","allium sativum","Musca domestica","Testy fly")
print("print tuple:",scientific_names)
scientific_names=list(scientific_names)

print("printing list:")
scientific_names[2]="brinjal"
print(scientific_names)

print("printing tuple:")
scientific_names=tuple(scientific_names)
print(scientific_names)