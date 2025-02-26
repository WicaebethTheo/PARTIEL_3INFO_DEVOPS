def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class Calculator:

    def add(self, a, b):
        if not (is_number(a) and is_number(b)):
            return "Error: a and b must be numbers"
        return a + b

    def multiply(self, a, b):
        if not (is_number(a) and is_number(b)):
            return "Error: a and b must be numbers"
        return a * b

    def divide(self, a, b):
        if not (is_number(a) and is_number(b)):
            return "Error: a and b must be numbers"
        if b == 0:
            return "Error: division by zero"
        return a / b
