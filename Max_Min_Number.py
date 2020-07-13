#Max and min number prompt (with input error id)

largest_num=None
smallest_num=None

while True:
    num=input("Enter a number: ")
    if num == "done":
        break
    try:
        num= float(num)
    except:
        print("Invalid Input")
        continue
    if largest_num is None:
        largest_num=num
    elif num > largest_num:
        largest_num=int(num)
    if smallest_num is None:
        smallest_num=num
    elif num < smallest_num:
        smallest_num= int(num)
    else:
        continue
print("Maximum is",largest_num)
print("Minimum is",smallest_num)
