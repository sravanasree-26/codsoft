def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def remainder(x,y):
    return x % y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."
    

# Input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")

# User chooses operation
choice = input("Enter choice (1-5): ")

# Perform calculation based on user's choice
if choice == '1':
    result = add(a, b)
    operation = '+'
elif choice == '2':
    result = subtract(a, b)
    operation = '-'
elif choice == '3':
    result = multiply(a, b)
    operation = '*'
elif choice == '4':
    result = divide(a, b)
    operation = '/'
elif choice == '5':
    result = remainder(a,b)
    operation = '%'
else:
    result = "Invalid input"
    operation = ""

# Display the result
print(f"{a} {operation} {b} = {result}")
