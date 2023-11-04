# Given a list numbers write python code to find the largest and smallest in the list without using built-in function like max() or min()


a=[20,90,100,55,80,200,5000,100,101,400,502,79]


s =a[0]  # Initialize max_num with the first element of the list

for i in a:
    if i > s:
        s = i

print("The maximum number in the list is:", s)
x=[1,2,3,4,5]
a=[]
for i in x:
    a.append(i)
    a.extend([0,0,0])


print(a)

#genrate this series using 
     

    