def evaluate_expression(expression: str) -> float:
    """
    Safely evaluate a basic arithmetic expression.
    Supports +, -, *, / and decimal values.
    """
    allowed_chars = set("0123456789.+-*/() ")
    if not all(char in allowed_chars for char in expression):
        raise ValueError("Expression contains invalid characters")

    try:
        result = eval(expression, {"__builtins__": None}, {})
        return round(result, 6)
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")
