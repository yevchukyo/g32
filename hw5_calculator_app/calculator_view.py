class CalculatorView:
    @staticmethod
    def hello():
        print("Hi! It's me, Smart Calculator")
        return input("Type a formula or (h|q): ")

    @staticmethod
    def help_calc():
        print("""
        {'_'*70}
            Type a formula like:
                x + y    for addition
                x - y    for substraction
                x / y    for classic division
                x // y   for floor division
                x % y    remainder of the division
                x ** y   x to the power of y
         {'_'*70}        
            """)
