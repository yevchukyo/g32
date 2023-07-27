from calculator import Calculator

class CalculatorController:
    def __init__(self):
        self.calculator = Calculator()

    def calculate(self, formula):
        first_operand, operation, second_operand = self.parse_formula(formula)
        if first_operand is None or second_operand is None:
            return "Bad formula! Try again, please"
        try:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        except ValueError:
            return "Operands must be valid numbers!"
        

        operations = ['+', '-', '*', '/', '%', '**', '//']
        if operation not in operations:
            return "Operation not recognized!"

        try:
            if (operation == '/' or operation == '//' or operation == '%') and second_operand == 0:
                return "Can't divide by zero!"
          
            if operation == '+':
                return f'{first_operand} {operation} {second_operand} = {self.calculator.add(first_operand, second_operand)}'
            elif operation == '-':
                return f'{first_operand} {operation} {second_operand} = {self.calculator.subtract(first_operand, second_operand)}'
            elif operation == '*':
                return f'{first_operand} {operation} {second_operand} = {self.calculator.multiply(first_operand, second_operand)}'
            elif operation == '/':
                return f'{first_operand} {operation} {second_operand} = {self.calculator.divide(first_operand, second_operand)}'
            elif operation == '%':
                return f'{first_operand} {operation} {second_operand} = {self.calculator.remainder(first_operand, second_operand)}'
            elif operation == '**':
                return f'{first_operand} {operation} {second_operand} = {self.calculator.power(first_operand, second_operand)}'
            elif operation == '//':
                return f'{first_operand} {operation} {second_operand} = {self.calculator.floor_divide(first_operand, second_operand)}'
        except ValueError:
            return "Bad formula! Try again, please"

    def parse_formula(self, formula):
        formula = formula.lower()
        operations = ['+', '-', '*', '/', '%', '**', '//']
        for operation in operations:
            if operation in formula:
                operands = formula.split(operation)
                if len(operands) == 2:
                    return operands[0].strip(), operation, operands[1].strip()
        return None, None, None
