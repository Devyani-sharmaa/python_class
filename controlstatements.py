# # for i in range(1,11):
# #     if i==6 or i==7:
# #         continue
# #     print('5','*',i,'=',i*5)

# '''for i in range (1,52):
#     if i %3==0 and i%5==0:
#         print("divisible by 3 and 5 both")  
#     else'''

# for i in range(0,11):
#     if i%2!=0:
#         print(str(i)*i)
#     else:    
#         print(i)

# for i in range(6): 
#     print(str(i))

# a=0
# while a<10:
#     a=a+1
#     print('5','*',a,'=',a*5)
   
# lst=[]
# lst.append(0)
# print(lst)

# a=[]
# for i in range(0,11):
#     z=f"2*{i}={2*i}"
#     a.append(z)
  
# print(a)

# def abc():

#     print("devyani")
#     print("devansh")
#     print(3+5)
# abc()

# lst=['xyz',20,'devyani','car',9,'devansh']
# a=[]
# b=[]
# for i in lst:
#     if type(i)==int:
#         a.append(i)
#     else:
#         b.append(i)


# #print("interger",i)
# print(a)
# print(b)


# storing divisible by 2 and not in different lst
# lst=[2,4,3,6,4,1,7,8,9,20,22,34,45]
# a=[]
# b=[]
# for i in lst:
#     if i%2==0:
#         a.append(i) 
#     else:
#         b.append(i)
# print(a)
# print(b)


# A=["hello","missisipi","car","airoplan","bike","verygood"]
# a=[]
# for i in A:
#     if i==max(A):
#         A.append(i)
# print(a)

        
a = "this is a caar "
lst = []
st = ""

for i in a:
    if i == " ":
        lst.append(st)
        st = ""
    else:
        if i in st:
            pass
        else:
            st = st + i

print(lst)


# a = "hlo this is mre"

# if "me" in a:
#     print("ok")


