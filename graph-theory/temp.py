from abc import abstractmethod, ABC

class Polygon(ABC):
    def __init__(self, name):
        print("this is abstract super class")
        self.name = name
    
    @abstractmethod
    def noofsildes(self):
        pass
    
    def printpoly(self):
        self.noofsildes()


class Triangle(Polygon):
    def __init__(self, name):
        print("this is subclass")
        super().__init__(name)
        
    def noofsildes(self):
        print("i have 3 sides")
        print("accessing parent class attribute in child class", self.name)
        

x = Triangle('hello')
x.printpoly()
print(x.name)


# from abc import ABC, abstractmethod
 
# class AbstractClassExample(ABC):
    
#     def __init__(self):
#         print("this is abstract super class")
    
#     @abstractmethod
#     def do_something(self):
#         print("Some implementation!")
        
        
        
# class AnotherSubclass(AbstractClassExample):
    
#     def __init__(self):
#         print("this is subclass")
#         super().__init__()

#     def do_something(self):
#         super().do_something()
#         print("The enrichment from AnotherSubclass")
        
# x = AnotherSubclass()
# x.do_something()
        