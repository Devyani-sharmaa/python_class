

'''Exception handeling:
    1) Compile time error (syntex error)
    2) Loigical error
    3) RUn time error
'''
a=10
print(a)

if 10 ==10:
    print("hello")


#2)Logical erros :

a = 10
b = 0

c = a / b

print(c)




#3) run time error:



age = int(input("Enter your age : "))


a = 10
b = "helo"

c = a + b
print(c)

print("heloo")


print("imp code")

print("done")


try:
    # try this  code

except Exception as e:
    # haddinling erros

else:
    # execute only when their is no error in try

finally:
    # indicate exeception andeling is doone.



a = 10
b = 0


age = int(input("ENter your age: "))

try:
    age = int(input("ENter your age: "))

except ValueError:
    print("Enter somthing vaild value")

except ZeroDivisionError:
    print("you cant devide 0 with anything")
    
except Exception as e:
    print(e)
    
else:
    print(age)

finally:
    print("error handle sucessfully")

print("code.....")

print("running")
