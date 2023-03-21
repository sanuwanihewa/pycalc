# perform simple arithmetic encoded in an input string
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    if operator == '+':
        return int(num0) + int(num1)
    elif operator == '-':
        return int(num0) - int(num1)
    elif operator == '*':
        return int(num0) * int(num1)
    else:
        print('unknown operator!')
        return None
