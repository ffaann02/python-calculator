class Calculator:
    def add(self, a, b):
        return a + b

    # bugs: switch from: b - a => a - b
    def subtract(self, a, b):
        return a - b

    # bugs: remove extra loop, handle minus number
    def multiply(self, a, b):
        positive_a = a
        positive_b = b
        if a<0:
            positive_a = -a
        if b<0:
            positive_b = -b
        result = 0
        for _ in range(positive_b):
            result = self.add(result, positive_a)
        if a<0 and b>0:
            result = -result
        elif b<0 and a>0:
            result = -result
        
        return result

    # bugs: handle with zero divider, replace > with => in while condition
    def divide(self, a, b):
        if b==0:
            raise ValueError("can't divide by zero")
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    # bugs: handle mod zero ,change condition in while loop to opposite
    def modulo(self, a, b):
        if b==0:
            raise ValueError("can't mod by zero")
        while a >= b:
            a = self.subtract(a, b)
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))