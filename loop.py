largest = None
smallest = None

while True :
    innum = input("Enter a number: ")
    if innum == "done" :
        break

    try:
        num = int(innum)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
