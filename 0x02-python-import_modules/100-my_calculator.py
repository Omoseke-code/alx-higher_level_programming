#!/usr/bin/python3
"""a simple claculator"""
if __name__ == "__main__":
    import calculator_1
    import sys

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print(f"{a} + {b} = ", calculator_1.add(a, b))
    elif sys.argv[2] == '-':
        print(f"{a} - {b} = ", calculator_1.sub(a, b))
    elif sys.argv[2] == '*':
        print(f"{a} * {b} = ", calculator_1.mul(a, b))
    elif sys.argv[2] == '/':
        print(f"{a} / {b} = ", calculator_1.div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
