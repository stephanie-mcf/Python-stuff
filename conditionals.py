mark = float(input("Please enter mark: "))

if 65 < mark < 75:
    print("Pass")
elif 75 < mark < 85:
    print("Distinction")
elif mark > 85:
    print("Merit")
else:
    print("Fail")


