class Apple:
    def show(self):
        print("Redish Apple!")


class Variety(Apple):
    def info(self):
        print("McIntosh")


v=Variety()
a=Apple()


#Calling the 
a.show()
v.info()