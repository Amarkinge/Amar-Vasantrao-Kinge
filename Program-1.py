class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


a = float(input("Enter the a value "))
b = float(input("Enter the b value "))
op = input("Enter type of operation (Addition, Substraction, Multiplication, Division): ")

c = Calculator()

if op == "Addition":
    print(c.add(a, b))
elif op == "Substraction":
    print(c.sub(a, b))
elif op == "Multiplication":
    print(c.mul(a, b))
elif op == "Division":
    print(c.div(a, b))
else:
    print("Invalid operation")
