def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, returning None if the denominator is zero.
    """
    #numerator = input("Enter the numerator: ")
    #denominator = input("Enter the denominator: ")
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
        
    if denominator == 0:
        return "Error: Cannot divide by zero."
        
    return f"The result of the division is {numerator / denominator}"