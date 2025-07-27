def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Check for division by zero
        if num2 == 0:
            # Return a specific message instead of just printing
            return "Cannot divide by zero."
        else:
            return num1 / num2
    else:
        # Return a message for invalid operations
        return "Invalid operation."