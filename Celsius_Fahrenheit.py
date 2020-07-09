# Celsius (C) to Fahrenheit (F)

conv = input('Enter "C to F" or "F to C"')

conv=conv.strip() # Stips any whitespace from entry, other than internal spaces.

while True:
    try: # Allows us to safely run code if user inputs any invalid data.
        if conv == "C to F": # Takes user input to determine what parameter they know.
            cel = float(input('Enter degrees Celsius: '))
            break
        elif conv == "F to C":
            far = float(input('Enter degress Fahrenheit: '))
            break
    except: # A way to tell the user they are entering the wrong data.
        print('Invalid Input. Please enter "C to F" or "F to C"')
        continue

if conv == "C to F": # Determines what expression to run based on user input.
    far = (cel * 9/5) + 32
else:
    cel = ((far - 32) * 5)/9

print("\tCelsius: ", int(cel),"C","\n","\tFahrenheit: ",int(far),"F")
