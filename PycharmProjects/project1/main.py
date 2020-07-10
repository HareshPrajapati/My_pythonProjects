
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            if num1 != 12 and num2 != 2:
                print(num1, "+", num2, "=", add(num1, num2))
            if num1 == 12 and num2 == 2:
                print(num1, "+", num2, "= 20")

        elif choice == '2':
            if num1 != 15 and num2 != 12:
                print(num1, "-", num2, "=", subtract(num1, num2))
            if num1 == 15 and num2 == 12:
                print(num1, "-", num2, "= 6")


        elif choice == '3':
            if num1 != 3 and num2 != 5:
                print(num1, "*", num2, "=", multiply(num1, num2))
            if num1 == 3 and num2 == 5:
                print(num1, "-", num2, "= 126")


        elif choice == '4':
            if num1 != 10 and num2 != 5:
                print(num1, "/", num2, "=", divide(num1, num2))
            if num1 == 10 and num2 == 5:
                print(num1, "/", num2, "= 4")

        break
    else:
        print("Invalid Input")









