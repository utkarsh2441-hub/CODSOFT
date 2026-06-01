#Simple Calculator

print("Welcome to the Simple Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))    

print("\nSelect the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice 1,2,3,4: ")

if choice == '1':
    sum = num1 + num2
    result = sum
    print(f"The result of {num1} + {num2} is: {result}")

elif choice == '2':
    difference = num1 - num2
    result = difference
    print(f"The result of {num1} - {num2} is: {result}")

elif choice == '3':
    product = num1 * num2
    result = product
    print(f"The result of {num1} * {num2} is: {result}")

elif choice == '4':
    if num2 != 0:
        quotient = num1 / num2
        result = quotient
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please select a valid operation (1, 2, 3, 4).")   