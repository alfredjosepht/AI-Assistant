def calculator(expression):

    try:
        return eval(expression)

    except Exception:
        return "Invalid expression"