#FUNCTIONS:code optimization
#declaration of function
'''def xyz():
    print("hello devyani")
xyz()    #call the function'''

##function have two methods i)parameters  ii)arguments
'''def sumthis(a,b):
    c=a+b
    print(c)
sumthis(10,2)'''


#parameters is of four types i)default parameter, ii)keyword parameter  iii)*args=()   iv)**kargs={}
'''def xyz(a=0,b=0):
    z=a+b
    print(z)
xyz(12,8)

def saveinfo(a,b):
    print(f"username {a} and user age {b}")
saveinfo(b=12,a="devyani")'''

#*args=()  samj nhi aaye
'''def sumthis(*args):
    b=0
    print("user entered:",args)
    for i in args:
        b=b+1
    print(b)
sumthis(10,20,22)'''


##**kargs
'''def xyz(**a):
    print(a)
xyz(name="car",agr=90,number=6789)'''


#compersion==[expression: loop:condition]   galat h program
'''zx=[i for i in range(1,20)if i %2==0]
print(zx)


num=int(input("enter the firstv number:"))
def xyz(*args):
    print(args)
choice=[int(input(f"enter how many values you wants too enter:"))]
zx=[int(input(f"enter {i+1}number:"))for i in range(choice)]
z=tuple(zx)
xyz(*zx)'''


#lambda function  *map()  *filter()  *reduce()
'''def xyz(a,b):
    c=a+b
    print(c)
xyz(12,10)'''

#lambda arguments:expression
'''zx=lambda a,b:a+b
print(zx(12,10))'''

'''z=lambda a:a**2
print(z(52))'''

#map(function,itraror)
'''lst=[2,3,4,5,6,7,8,9,10]
zx=map(lambda v:v+10,lst)
print(list(zx))'''


#filter function(function,itrator) 
'''k=[1,2,3,4,4,5,6,7,8,9,9]
zx=filter(lambda a:a%2==0,k)
print(tuple(zx))'''

#reduce
'''k=[1,2,3,4,5,6,7,8,9]
from functools import reduce
zx=reduce(lambda a,b:a+b,k)
print(zx)'''


#decorator
'''def decorator(i):
    def abc():
        print("welcome to my function")
        i()
        print("rthank you")
    return abc
@decorator
def xyz():
    print("hello world")
xyz()'''



# a=[1,2,2,3,1,4,4,4,5,1,1]
# # zx=[i for i in range(1,20)if i.count==i]
# # print(zx)
# b=a.count(1)
# c=a.count(2)
# d=a.count(3)
# e=a.count(4)

# print(b)
# print(c)
# print(d)
# print(e)

# def suminfo(**kagrs):
#     print(kagrs)
# suminfo(one={b},two={c},three={d},four={e})
     


#b=[1,2,2,3,1,4,4,4,5,1,1] find the count for indivaadual

def xyz(*x):
    lst=list(x)
    dic={}

    for i in lst:
        if i not in dic and lst.count(i)!=1:
            dic[i]=lst.count(i)
    print(dic)
xyz(1,2,3,3,4,1,2,3,2,4,3,6,4)





