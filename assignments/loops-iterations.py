largest = 1
smallest = 5
while True:
    num_str= input("Enter a number: ")
    try:
        int(num_str)
        num = int(num_str)
    except:
        if num_str == "done":
            break
        else:
            print("Invalid input")
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)
