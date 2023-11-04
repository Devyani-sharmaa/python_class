# a=open("mydata.txt","r")
# print(a.read())
# print(a.readline())#first line

# a.close()


# #how to write in file----its will delete the previous data
# x=open("mydata.txt","w")
# x.write("hello i am good")


# it will append the data means previous data remain same
# x=open("mydata.txt","a")
# x.write("hello i am good")



# a=34567890
# y=open("mydata.txt","a")
# y.write(f"\n " {a})#galat h 




# y.close()




# x=open("mydata.txt","a")
# x.write(input("Enter name : "))

# y=open("uhv.txt","a")
# y.write(input("u name"))

# z=open("name.txt","a")
# z.write(x+y)

#ques- make a file a and b and then store it to c



a = input("Enter name 'a': ")
x=open('mydata.txt', 'w')
x.write(a)
x.close()



b = input("Enter name 'b': ")
y= open('uhv.txt', 'w')
y.write(b)
y.close()



z=open('mydata.txt', 'r')
z1=z.read()
z.close()


v=open('uhv.txt', 'r')
z2=v.read()
v.close()
# print(z1,z2)
w=int(z1)+int(z2)
we=open("result.txt","w")
we.write(str(w))
we.close()








