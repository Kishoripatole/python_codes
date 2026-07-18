class Textbook:
     def info(self):
          print("Hello, textbook")
          


class Library:
      def appear(self):
           print("hello,notebook")
        
    

class name_of_book(Textbook,Library):
        def show(self):
          print("hello,roughbook")

t=name_of_book()

t.show()
t.info()
t.appear()



