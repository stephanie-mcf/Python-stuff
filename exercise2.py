name = input("Enter name: ")
salary = int(input("Enter salary: "))

if salary >= 1500:
    tax = salary * 21/100
else:
    tax = salary * 10/100
net = salary - tax
print(name)
print(tax)
print(net)