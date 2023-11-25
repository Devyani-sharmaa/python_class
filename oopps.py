# class
# object
# self 
# contructor
# methods
# inhertience-simple,multple,multilevel,hirarical,hydrid
# abraction  -abstract class,abstract methods

#class and object
'''class xyz:
    def method1(self):
        print("devyani")
    def method2(self):
        print("devansh")
object=xyz()
object.method1()'''

#constructor
'''class xyz:
    def __init__(self,a,b):
        self.num1=a#ATTRIBUTES
        self.num2=b
    def method1(self):
        print("hello")
    def method2(self):
        print("devansh")
    def sumthis(self):
        c=self.num1+self.num2
        print(c)
obj=xyz(10,20)
obj.method1()
obj.sumthis()'''



#inheritamce simple
'''class abc:
    def method1(self):
        print("devyani")
    def method2(self):
        print("devansh")

class xyz(abc):
    def method3(self):
        print("jyoti")


obj=xyz()
obj.method3()
obj.method2()'''

#multipe 
'''class abc():
    def method1(self):
        print("hello")
class xyz():
    def method2(self):
        print("hey")
class dev(abc,xyz):
    def method3(self):
        print("meo")
object=dev()
object.method1()'''
       

#multilevel
'''
class abc():
    def method1(self):
        print("hello")
class xyz(abc):
    def method2(self):
        print("hey")
class uhv(xyz):
    def method3(self):
        print("meo")
object=uhv()
object.method1()
object.method3()
'''

#herichal

'''class abc:
    def method1(self):
        print("hello")
class xyz(abc):
    def method2(self):
        print("hey")
class dev(abc):
    def method3(self):
        print("meo")
object=dev()
object.method1()'''




#hybrid
'''class abc:
    def method1(self):
        print("hello")
class xyz():
    def method2(self):
        print("hey")
class dev(xyz,abc):
    def method3(self):
        print("meo")
class non(dev):
    def method4(self):
         print("ghjk")
class wer(non):
    def method5(self):
        print('asd')

obj=wer()
obj.method1()
obj.method5()
'''


#super
'''class abc:
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.number=c
    def saveinfo(self):
        print(f"save data of user name={self.name},age={self.age}and number={self.number}")

obj1=abc("dev",2,12334)
obj2=abc("we",2,2345)


obj1.saveinfo()
class xyz(abc):
    def __init__  (self, a, b, c,d):
         super().__init__(a, b, c)
         self.address=d
    def saveinfo(self):
        print(f"save data of user name={self.name},age={self.age},number={self.number},address={self.address}")
    
obj3=xyz("asxdf",2,234,"dfghjk")
obj3.saveinfo()'''



import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", 
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

# Better to use This source Code on pycharm!


