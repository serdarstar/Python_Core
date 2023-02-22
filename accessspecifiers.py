"""
Public # can be accessed from everywhere

Protected  - _   _var, def _method() # can be accessed within the class and derived classes

Private - __var, def __method() # can be accessed within the class only


"""

class Car:
    publicVar = 9
    _protectedVar = 10
    __privateVar = 11

    def __init__(self):
        print("Inside Car constructor")

    def publicMethod(self):
        print("Calling public method")


    def _protectedMethod(self):
        print("Calling protected method")



    def __privateMethod(self):
        print("Calling private method")
