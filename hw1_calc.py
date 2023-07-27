TITLE = 'Smart Calculator'

separators = ['+','-','*','/','%','**','//']
first_operand = second_operand = 0
operation = ''
result = ''
def hello ():
    #print ("Hi! Its me," + TITLE)
    print (f"Hi! Its me, + {TITLE}")
    return input ("Type a formula or (h|q)")
def help_calc():
    print (f"""  
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
while True:
    formula = hello()
    formula = formula.lower()

    if formula.startswith('q') or formula.startswith('h'):
        formula = formula[0:1]
    match formula:
        case 'h':
            help_calc()
        case 'q' | 'exit':
            print(F'Thank You for using {TITLE}')
            break
        case _:
            for sep in separators:
                   if len(formula.split(sep)) == 2:
                    first_operand, second_operand = formula.split(sep)
                    first_operand = first_operand.strip()
                    second_operand = second_operand.strip()
                    
                    if first_operand.isdigit():
                        first_operand = float (first_operand)
                    else: 
                        result = f"{first_operand} is not a number"   
                        break      
                    if second_operand.isdigit():
                        second_operand = float (second_operand)
                        if second_operand == 0 and sep in ('/', '//','%'):
                            result = "Can't divide by zero!"
                            break
                    else: 
                        result = f"{second_operand} is not a number"
                        break
                    operation = sep  
# ['+','-','*','/','%','**','//']
                    match operation:
                        case '+':
                            res = first_operand + second_operand
                        case '-':
                            res = first_operand - second_operand
                        case '*':
                            res = first_operand * second_operand
                        case '/':
                            res = first_operand / second_operand
                        case '%':
                            res = first_operand % second_operand
                        case '**':
                            res = first_operand ** second_operand
                        case '//':
                            res = first_operand // second_operand  
                        case _:
                            res = 'Operation not recognized!'
                    #print(first_operand, second_operand)
                    result =f'{first_operand} {operation} {second_operand} = {res}'
                    break
            else:
                result = "Bad formula! Try again, please"
            print (f"Here You are: {result}")

