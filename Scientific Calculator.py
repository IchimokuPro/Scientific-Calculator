import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def main():
    print("Scientific Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice in ['1', '2', '3', '4', '5']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    else:
        x = float(input("Enter number: "))

    if choice == '1':
        print("Result:", add(x, y))
    elif choice == '2':
        print("Result:", subtract(x, y))
    elif choice == '3':
        print("Result:", multiply(x, y))
    elif choice == '4':
        print("Result:", divide(x, y))
    elif choice == '5':
        print("Result:", power(x, y))
    elif choice == '6':
        print("Result:", sqrt(x))
    elif choice == '7':
        print("Result:", sin(x))
    elif choice == '8':
        print("Result:", cos(x))
    elif choice == '9':
        print("Result:", tan(x))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
