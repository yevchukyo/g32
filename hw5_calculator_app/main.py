from calculator_view import CalculatorView
from calculator_controller import CalculatorController

if __name__ == "__main__":
    calculator_view = CalculatorView()
    calculator_controller = CalculatorController()

    while True:
        formula = calculator_view.hello()

        if formula.startswith('q') or formula.startswith('h'):
            formula = formula[0:1]
        if formula == 'h':
            calculator_view.help_calc()
        elif formula == 'q' or formula == 'exit':
            print("Thank You for using Smart Calculator")
            break
        else:
            result = calculator_controller.calculate(formula)
            print(f"Here You are: {result}")