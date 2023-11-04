# # print string into list
'''a = "this is a caar "
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
            st = st + i #this

print(lst)'''


# # 
a = "hlo this is mre"

if "me" in a:
    print("ok")



A=["hello","missisipi","car","airoplan","bike","verygood"]
lst = []
st=""

for i in A:
    for j in i:
           if i.count(j)!=1:
                  continue
           else:
                   print("ok")
    
print(lst)

#compersion==[expression: loop:condition]
# : print table of 2 

'''xyz=[f"2*{i}={2*i}" for i in range(1,11) if i!=5]
print(xyz) '''