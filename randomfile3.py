control = int(input("Select option"))
while control:
    print("Menu: press 1 to continue, press 2 to exit!")
    var1 = int(input("Please enter a number: "))

    if var1 == 1:
        control = True
    elif var1 == 2:
        control = False
    else:
        print("Invalid! Please try again!")
