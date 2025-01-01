import re

def parse_expression(expression):
    expression = expression.replace(" ", "")  # remove spaces
    valid_chars = set("0123456789+-*/().")
    for char in expression:
        if char not in valid_chars:
            raise ValueError(f"Invalid character in expression: {char}")
    return expression

def tokenize(expression):
    pattern = r"(\d+\.\d+|\d+|[+\-*/()^])"  # Match numbers, operators, and parentheses
    tokens = re.findall(pattern, expression)
    return tokens

def to_postfix(tokens):
    precedence = {
        "+": 1, "-": 1,
        "*": 2, "/": 2,
        "^": 3  # Power operator has higher precedence
    }
    output = []
    operators = []

    for token in tokens:
        if token.isdigit() or re.match(r"\d+\.\d+", token):  # Number
            output.append(token)
        elif token in "+-*/^":  # Operators
            while (operators and operators[-1] != '(' and precedence.get(token, 0) <= precedence.get(operators[-1], 0)):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Remove the matching '(' from the stack
    while operators:
        output.append(operators.pop())

    return output

def validate_postfix(postfix_tokens):
    operand_count = 0
    for token in postfix_tokens:
        if token.isdigit() or re.match(r"\d+\.\d+", token):
            operand_count += 1
        elif token in "+-*/^":
            if operand_count < 2:
                raise ValueError("Invalid postfix expression: insufficient operands")
            operand_count -= 1
        else:
            raise ValueError(f"Invalid token in postfix expression: {token}")
    if operand_count != 1:
        raise ValueError("Invalid postfix expression")

def evaluate_postfix(postfix_tokens):
    validate_postfix(postfix_tokens)
    
    stack = []
    
    for token in postfix_tokens:
        if re.match(r"\d+\.\d+|\d+", token):
            stack.append(float(token))
        elif token in "+-*/^":
            if len(stack) < 2:
                raise ValueError("Insufficient operands in expression")
            b = stack.pop()
            a = stack.pop()
            if token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                result = a / b
            elif token == "*":
                result = a * b
            elif token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "^":  # Exponentiation
                result = a ** b
            stack.append(result)
        else:
            raise ValueError(f"Unknown token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()

def evaluate_expression(expression):
    parsed = parse_expression(expression)
    tokens = tokenize(parsed)
    postfix = to_postfix(tokens)
    result = evaluate_postfix(postfix)
    return result

if __name__ == "__main__":
    expression = "(8 / 4) + (10 / (2 * 5))"
    try:
        result = evaluate_expression(expression)
        print(f"The result of '{expression}' is: {result}")
    except Exception as e:
        print(f"Error: {e}")
