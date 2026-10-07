mydict1={}
while True:

    key=input("enter a key(or'q' to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict1[key]=value
print('orgiinal dictionary 1:',mydict1)
mydict2={}
while True:

    key=input("enter a key(or'q' to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict2[key]=value
print('orgiinal dictionary 2:',mydict2)
print("merged dictonary=",mydict1|mydict2)
