text_book={1:"Mathematics and statistic",2:"Chemistry",3:"Biology",4:"Geography"}

print(text_book)

#by using del keyword
del text_book[3]
print("Removing Biology subject:",text_book)

#by using pop() function
removed_element=text_book.pop(1)

print("Delets random element:",removed_element)

#by using popitem function
removing_last_item=text_book.popitem()
print("Removing last element:",removing_last_item)

#Clear function
text_book.clear()
print("Empty dictionary:",text_book)