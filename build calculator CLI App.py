# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    print("===== Command-line Calculator =====")
    print("Available operations: +  -  *  /")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator!")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
