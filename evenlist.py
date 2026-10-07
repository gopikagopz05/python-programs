num=int(input("enter limit"))
list=[]
for i in range(num):
    list.append(int(input("enter elements")))

for i in list:
    if(i%2==0):
        list.remove(i)

print("list removing even numbers")
print("list=",list)

