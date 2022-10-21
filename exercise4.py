name = input("Enter name: ")
salary = int(input("Enter salary "))

if salary >= 3000:
    tax = salary * 21/100
else:
    if salary >2000:
        tax = salary * 15/100
    else:
        if salary >= 1000:
            tax = salary *10/100
        else:
            tax = 0
net = salary - tax

print(name)
print(tax)
print(net)