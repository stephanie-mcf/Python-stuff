physics = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))
maths = int(input("Enter maths marks: "))

total = physics + chemistry + maths 
percentage = total / 450 * 100

if percentage >= 60:
    print("pass")
else:
    print("fail")