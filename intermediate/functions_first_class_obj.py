# Functions  inputs/functionality/output

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


# Functions are first class objects (pass as argument and also returned)
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


# another example of how we can get an inner function:
def outer_f():
    print("_outer_")

    def inner_f():
        print("_inner_")

    return inner_f


def main():
    print(
        operations["*"](5, 2)
    )

    print(
        calculate(operations["+"], 2, 3)
    )

    returned_inner_f = outer_f()
    returned_inner_f()




if __name__ == "__main__":
    main()