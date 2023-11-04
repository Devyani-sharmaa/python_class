#how to count the interger number
'''a = "2349283496131231928"

print(a.count("2"))#must be str, not int'''

# #ques-Write a Python function that takes multiple arguments, processes them, and 
# returns a dictionary containing duplicate values as keys and their respective 
# counts as values. The function should convert the input arguments to a list and 
# then identify and count the duplicate values. Output : For example, if the function
#  is called with arguments (1, 2, 2, 3, 1, 4, 4, 4, 5, 1, 1), it should
#  return {1 : 4, 2 : 2, 4 : 3}
'''def xyz(*x):
    lst = list(x)
    dic = {}
    
    for i in lst:
        if i not in dic and lst.count(i) != 1:
            dic[i] = lst.count(i)
    
    print(dic)

xyz(1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 5)'''




#  Abstration : 
#      1) Abs

# abc => abstract base class
'''
from abc import ABC, abstractmethod
# interface--all abstract method in abstract class is called interface
class cls1(ABC):
    @abstractmethod
    def mthd1(self):
        pass
    
    @abstractmethod
    def mthd2(self):
        pass
        
class cls2(cls1):
    def car(self):
        print("this is a car")
    
    def mthd1():
        print("askjdsakd")

x = cls2()
x.car()
'''


# Encapsulation : when you bind multipal things in a single unit.

# Access SApcifires :
    # 1) puclic mambers
    # 2) protected mambes _
    # 3) privare mambers

# 1) puclic mambers
'''
class cls1:
    def _init_(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def mthd1(self):
        print("this is thd1")
    
    def mthd2(self):
        print("this is mthd2")
        
class cls2(cls1):
    def car(self):
        print("this is a car")
    


x = cls1(10, 20)
print(x.num1)


# proteted mambers:   within class or subclasss   _

# class cls1:
#     def _init_(self, a, b):
#         self._num1 = a
#         self.num2 = b
    
#     def mthd1(self):
#         print("this is thd1")
    
#     def mthd2(self):
#         print("this is mthd2")
        
# class cls2(cls1):
#     def _car(self):
#         print("this is a car")
    

# x = cls2(10, 20)
# # print(x._num1)
# x._car()
'''


# 3) private mambers : asscable witin calss  __
    
'''
class cls1:
    def _init_(self, a, b):
        self.__num1 = a
        self.num2 = b
    
    def mthd1(self):
        print(self.__num1)
    
    def mthd2(self):
        print("this is mthd2")
        
class cls2(cls1):
    def _car(self):
        print("this is a car")
    

x = cls1(10, 20)
# print(x.__num1)
x.mthd1()
'''


# 4) Polymorpiusm:
    # poly = many
    # morphiusm = forms
    
    # 1) compile time polymorum
    #     1) operater overloading
    #     2) method overloading
        
    # 2) run time polymorphisum
    #     1) method overriding


# a = 10

# a = 40

# print(a)


'''   
class cls1:
    def mthd1(self):
        print("this is mthod 1")
    
    def mthd2(self):
        print("this is mthd2")
        
class cls2(cls1):
    def mthd3(self):
        print("this is a car")
    
    def mthd1(self):
        print("newwewe mejwd")


obj = cls2()
obj.mthd1()


'''
'''
class cls1:
    def _init_(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def car(self):
        print("nootskdjf")
    
    def _add_(x, y):
        zx = x.num1 + y.num1
        qw = x.num2 + y.num2
        er = cls1(zx, qw)
        return er

obj1 = cls1(10, 20)
obj2 = cls1(13, 70)

c = obj1 + obj2

print(c.num2)'''



# how to return the function
'''def xyz():
    a = 10
    return a

zx = xyz()
    
print(zx)'''





# Method overloading:

# class cls1:
#     def sumthis(self, a, b, c):
#         zx = a + b + c
#         print(zx)
    
#     def sumthis(self, a, b):
#         zx = a + b 
#         print(zx)
    
#     def sumthis(self, a):
#         zx = a
#         print(zx)

# obj = cls1()
# obj.sumthis(7, 3)

# a = 10
# a = 40



# how to achive method overlaoding:
'''
class cls1:
    def sumthis(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            zx = a + b + c
            print(zx)
        
        elif a != None and b != None:
            zx = a + b 
            print(zx)
        
        elif a != None :
            zx = a 
            print(zx)

obj = cls1()
obj.sumthis(7, 10, 9)
'''