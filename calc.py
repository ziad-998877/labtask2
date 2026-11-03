def calculate(a, b, operation):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    if operation == "+":
        return a + b


def main():

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculate(a, b, operation)
            print("Result:", result)
   