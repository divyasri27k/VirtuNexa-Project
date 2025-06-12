from calculator import core, history_db

def calculator_mode():
    history_db.init_db()
    print("Basic Calculator\n")
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Operation (+ - * /): ")
            b = float(input("Enter second number: "))
            if op == '+':
                result = core.add(a, b)
            elif op == '-':
                result = core.subtract(a, b)
            elif op == '*':
                result = core.multiply(a, b)
            elif op == '/':
                result = core.divide(a, b)
            else:
                print("Invalid operator")
                continue
            print(f"Result: {result}")
            history_db.log_to_db(op, a, b, result)
        except Exception as e:
            print(f"Error: {e}")
        if input("Continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    calculator_mode()