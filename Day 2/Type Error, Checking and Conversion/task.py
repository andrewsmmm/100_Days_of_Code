length = len (str(12345))
print (length)

print(type("12345"))

print(type(1232))

print(type(123.45))

print(type(False))

print(int("123")+int("123"))
print(int("123")+123)
print()
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
print()
fahr = float(input("Enter temperature in Fahrenheit: "))
try:
    celsius = (fahr - 32) * 5.0/9.0
    print(f"{fahr} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
except:
    print("Invalid input. Please enter a numeric value for Fahrenheit.")