def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# ! we can assign a function reference as a value in a dictionary

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def main():
    print(operations["*"](5, 2))

if __name__ == "__main__":
    main()