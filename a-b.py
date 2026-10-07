list1=set()
list2=set()
n1=int(input("enter number of colors"))
print("enter the colour of list1")
for i in range(n1):
    list1.add(input())

n2=int(input("enter number of colors"))
print("enter the colour of list2")
for i in range(n2):
    list2.add(input())

print("COLOURS IN LIST1 NOT IN LIST2=",list1-list2)
    
