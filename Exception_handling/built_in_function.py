class CustomException(BaseException):  
    def __init__(self, message):  
        self.message = message  
          
    def __str__(self):  
        return f"This is so good feeling{self.message}"  
try:
    raise CustomException("This is a custom exception.")
except CustomException  as e:
    print("Exception is there !" )