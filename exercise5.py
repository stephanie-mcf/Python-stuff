a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

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