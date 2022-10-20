a = int(input("please enter a number: "))
b = int(input("please enter a number: "))
c = int(input("please enter a number: "))

if a > b: 
    if a > c:
     print(a)   
    else: 
        print(c)
else:
    if b > c: 
        print(b)
    else:
        print(c)